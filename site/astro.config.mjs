import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { prefixInternalLinks } from './src/lib/base-links.mjs';

export default defineConfig({
  site: process.env.SITE_URL || 'https://8b-is.github.io',
  base: process.env.SITE_BASE || '/',
  integrations: [
    mermaid({
      theme: 'dark',
      autoTheme: true,
      mermaidConfig: {
        theme: 'dark',
        flowchart: { curve: 'basis' },
      },
    }),
    starlight({
      title: '8b Library',
      description:
        'Documentation for the 8b.is / Ayeverse stack — MEM|8, AyeOS, Ayevn, Smart Tree, and MEMNET.',
      logo: {
        src: './src/assets/logo.svg',
        alt: '8b.is',
      },
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/8b-is/8b-public-documents' },
      ],
      customCss: ['./src/styles/ayeverse.css', 'katex/dist/katex.min.css'],
      head: [
        { tag: 'meta', attrs: { name: 'theme-color', content: '#060402' } },
        {
          tag: 'link',
          attrs: {
            rel: 'preconnect',
            href: 'https://fonts.googleapis.com',
          },
        },
        {
          tag: 'link',
          attrs: {
            rel: 'preconnect',
            href: 'https://fonts.gstatic.com',
            crossorigin: true,
          },
        },
        {
          tag: 'link',
          attrs: {
            rel: 'stylesheet',
            href: 'https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Newsreader:opsz,wght@6..72,500;6..72,650&display=swap',
          },
        },
      ],
      expressiveCode: {
        themes: ['houston', 'min-light'],
      },
      pagination: false,
      sidebar: [
        { label: 'Library', items: [
          { label: 'Explore the collection', slug: 'explorer' },
          { label: 'Reading paths', slug: 'collections' },
          { label: 'Guardian playground', slug: 'playground' },
          { label: 'Evidence & editions', slug: 'evidence' },
          { label: 'Downloads', slug: 'downloads' },
          { label: 'Accessibility', slug: 'accessibility' },
        ] },
        {
          label: 'Start here',
          items: [
            { label: 'Quick Reference', slug: 'quick-reference' },
            { label: 'Hub README', slug: 'readme' },
            { label: 'Navigation', slug: 'navigation' },
          ],
        },
        {
          label: 'Architecture',
          items: [
            { label: 'Architecture', slug: 'architecture' },
            { label: 'Integration', slug: 'integration' },
            { label: 'Glossary', slug: 'glossary' },
          ],
        },
        {
          label: 'Learn by example',
          items: [{ label: 'Use cases', slug: 'use-cases' }],
        },
        {
          label: 'MEM|8',
          items: [
            { label: 'Overview', slug: 'mem8/overview' },
            { label: 'Technical paper', slug: 'mem8/mem8-paper' },
            { label: 'January paper', slug: 'mem8/mem8-paper-january' },
            { label: 'Temporal philosophy', slug: 'mem8/mem8-temporal-philosophy' },
            { label: 'vs Wave-RNN', slug: 'mem8/mem-8-vs-wrnn' },
          ],
        },
        {
          label: 'AyeOS / Ayevn',
          items: [
            { label: 'MEMNET protocol', slug: 'ayeos/ayeos-memnet-protocol' },
            { label: 'Ayevn overview', slug: 'ayeos/ayevn/overview' },
            { label: 'Ayevn spec', slug: 'ayeos/ayevn/ayevn-spec' },
            { label: 'MEM|8 integration', slug: 'ayeos/ayevn/ayevn-mem8-integration' },
            { label: 'Ayevn reference', slug: 'ayeos/ayevn/ayevn-reference' },
          ],
        },
        {
          label: 'Smart Tree',
          items: [
            { label: 'Overview', slug: 'smart-tree/overview' },
            { label: 'Catalog', slug: 'smart-tree/catalog' },
            { label: 'Features', slug: 'smart-tree/features-overview' },
            { label: 'Philosophy', slug: 'smart-tree/smart-tree-philosophy' },
            { label: 'MCP guide', slug: 'smart-tree/mcp-guide' },
            { label: 'MCP quick reference', slug: 'smart-tree/mcp-quick-reference' },
            { label: 'Compression guide', slug: 'smart-tree/compression-guide' },
            { label: 'Mode selection', slug: 'smart-tree/mode-selection-guide' },
            { label: 'CLI cheatsheet', slug: 'smart-tree/st-cheetsheet' },
          ],
        },
        {
          label: 'Research',
          items: [
            { label: 'Research index', slug: 'research-index' },
            {
              label: 'Ultrasonic therapy',
              slug: 'ultrasonic-therapy/compressed-audio-patterns-and-emotional-resonance',
            },
            { label: 'Process-relational', slug: 'working/overview' },
            { label: 'Framework', slug: 'framework/overview' },
            { label: 'Forth experiments', slug: 'forth/overview' },
            {
              label: 'Working papers',
              items: [{ autogenerate: { directory: 'working' } }],
            },
          ],
        },
        {
          label: 'Philosophy',
          items: [{ label: '42: Imagination', slug: '42' }],
        },
        {
          label: 'Constellation',
          items: [{ label: 'Products', slug: 'constellation' }],
        },
      ],
    }),
  ],
  markdown: {
    remarkPlugins: [remarkMath, prefixInternalLinks],
    rehypePlugins: [rehypeKatex, prefixInternalLinks],
  },
});
