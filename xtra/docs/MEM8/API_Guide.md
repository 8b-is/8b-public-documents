# Mem|8 API Guide

## Overview

This guide provides comprehensive documentation for Mem|8's APIs. It covers API endpoints, request/response formats, authentication, error handling, and best practices for API usage.

## Core APIs

### Memory Grid API

```rust
/// Memory Grid Operations
pub trait MemoryGridApi {
    /// Create a new memory grid
    ///
    /// # Parameters
    /// - `width`: Grid width
    /// - `height`: Grid height
    /// - `config`: Grid configuration
    async fn create_grid(&self, width: u32, height: u32, config: GridConfig) -> Result<GridId, ApiError>;
    
    /// Read grid cell value
    ///
    /// # Parameters
    /// - `grid_id`: Grid identifier
    /// - `x`: X coordinate
    /// - `y`: Y coordinate
    async fn read_cell(&self, grid_id: GridId, x: u32, y: u32) -> Result<CellValue, ApiError>;
    
    /// Write grid cell value
    ///
    /// # Parameters
    /// - `grid_id`: Grid identifier
    /// - `x`: X coordinate
    /// - `y`: Y coordinate
    /// - `value`: Cell value
    async fn write_cell(&self, grid_id: GridId, x: u32, y: u32, value: CellValue) -> Result<(), ApiError>;
}

// Example Request
POST /api/v1/grids
{
    "width": 8,
    "height": 8,
    "config": {
        "cell_type": "BindCell",
        "temporal_enabled": true,
        "decay_rate": 0.1
    }
}

// Example Response
{
    "grid_id": "grid_12345",
    "status": "created",
    "timestamp": "2025-01-05T12:00:00Z"
}
```

### Temporal API

```rust
/// Temporal Operations
pub trait TemporalApi {
    /// Create temporal link
    ///
    /// # Parameters
    /// - `source`: Source cell coordinates
    /// - `target`: Target cell coordinates
    /// - `strength`: Link strength
    async fn create_link(&self, source: CellCoord, target: CellCoord, strength: f32) -> Result<LinkId, ApiError>;
    
    /// Query temporal relationships
    ///
    /// # Parameters
    /// - `cell`: Cell coordinates
    /// - `timespan`: Time range to query
    async fn query_temporal(&self, cell: CellCoord, timespan: TimeSpan) -> Result<Vec<TemporalRelation>, ApiError>;
    
    /// Update temporal strength
    ///
    /// # Parameters
    /// - `link_id`: Link identifier
    /// - `new_strength`: New link strength
    async fn update_strength(&self, link_id: LinkId, new_strength: f32) -> Result<(), ApiError>;
}

// Example Request
POST /api/v1/temporal/links
{
    "source": {
        "grid_id": "grid_12345",
        "x": 3,
        "y": 4
    },
    "target": {
        "grid_id": "grid_12345",
        "x": 5,
        "y": 6
    },
    "strength": 0.8
}

// Example Response
{
    "link_id": "link_67890",
    "status": "created",
    "timestamp": "2025-01-05T12:00:00Z"
}
```

### Memory Management API

```rust
/// Memory Management Operations
pub trait MemoryManagementApi {
    /// Store memory
    ///
    /// # Parameters
    /// - `memory`: Memory data
    /// - `config`: Storage configuration
    async fn store_memory(&self, memory: Memory, config: StorageConfig) -> Result<MemoryId, ApiError>;
    
    /// Retrieve memory
    ///
    /// # Parameters
    /// - `memory_id`: Memory identifier
    async fn retrieve_memory(&self, memory_id: MemoryId) -> Result<Memory, ApiError>;
    
    /// Update memory
    ///
    /// # Parameters
    /// - `memory_id`: Memory identifier
    /// - `updates`: Memory updates
    async fn update_memory(&self, memory_id: MemoryId, updates: MemoryUpdates) -> Result<(), ApiError>;
}

// Example Request
POST /api/v1/memories
{
    "data": {
        "content": "Example memory content",
        "type": "text",
        "tags": ["important", "reference"]
    },
    "config": {
        "storage_type": "long_term",
        "compression": "enabled",
        "encryption": "enabled"
    }
}

// Example Response
{
    "memory_id": "mem_24680",
    "status": "stored",
    "timestamp": "2025-01-05T12:00:00Z"
}
```

## Authentication

### Authentication Methods

```rust
/// Authentication Operations
pub trait AuthenticationApi {
    /// Authenticate request
    ///
    /// # Parameters
    /// - `credentials`: Authentication credentials
    async fn authenticate(&self, credentials: Credentials) -> Result<AuthToken, AuthError>;
    
    /// Validate token
    ///
    /// # Parameters
    /// - `token`: Authentication token
    async fn validate_token(&self, token: AuthToken) -> Result<bool, AuthError>;
    
    /// Refresh token
    ///
    /// # Parameters
    /// - `token`: Current authentication token
    async fn refresh_token(&self, token: AuthToken) -> Result<AuthToken, AuthError>;
}

// Example Request
POST /api/v1/auth/token
{
    "api_key": "your-api-key",
    "secret": "your-secret"
}

// Example Response
{
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "expires_at": "2025-01-05T13:00:00Z",
    "token_type": "Bearer"
}
```

## Error Handling

### Error Responses

```rust
/// API Error Types
#[derive(Debug, Serialize)]
pub enum ApiError {
    /// Authentication error
    AuthError(String),
    
    /// Validation error
    ValidationError(String),
    
    /// Resource error
    ResourceError(String),
    
    /// System error
    SystemError(String),
}

// Example Error Response
{
    "error": {
        "type": "ValidationError",
        "message": "Invalid grid coordinates",
        "details": {
            "x": "Must be less than grid width",
            "y": "Must be less than grid height"
        },
        "code": "INVALID_COORDS"
    }
}
```

## Rate Limiting

### Rate Limit Headers

```rust
/// Rate Limit Information
pub struct RateLimit {
    /// Maximum requests per window
    pub limit: u32,
    
    /// Remaining requests in current window
    pub remaining: u32,
    
    /// Window reset time
    pub reset: DateTime<Utc>,
}

// Example Response Headers
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1704460800
```

## Best Practices

### API Usage Guidelines

1. Authentication
   - Always use HTTPS
   - Keep credentials secure
   - Rotate tokens regularly

2. Request Handling
   - Validate input data
   - Handle errors gracefully
   - Implement retries

3. Performance
   - Use pagination
   - Minimize request size
   - Cache responses

### Security Guidelines

1. API Security
   - Use strong authentication
   - Implement rate limiting
   - Validate all input

2. Data Protection
   - Encrypt sensitive data
   - Use secure protocols
   - Implement access control

3. Monitoring
   - Log API usage
   - Monitor errors
   - Track performance

## Future Enhancements

### Planned Features

1. Enhanced APIs
   - GraphQL support
   - WebSocket APIs
   - Streaming APIs

2. Better Security
   - OAuth2 support
   - API key rotation
   - Enhanced monitoring

3. Improved Performance
   - Response caching
   - Request batching
   - Optimized queries
