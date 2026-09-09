/** Prefix authored links for a project Pages URL; idempotent across both AST passes. */
export function withBase(url, base = process.env.SITE_BASE || '') {
  const prefix = base.replace(/\/$/, '');
  if (!prefix || !url.startsWith('/') || url.startsWith('//') || url === prefix || url.startsWith(prefix + '/')) return url;
  return prefix + url;
}
export function prefixInternalLinks() {
  return tree => {
    const visit = node => {
      if (typeof node.url === 'string') node.url = withBase(node.url);
      if (node.properties) for (const key of ['href', 'src', 'poster']) {
        if (typeof node.properties[key] === 'string') node.properties[key] = withBase(node.properties[key]);
      }
      for (const attr of Array.isArray(node.attributes) ? node.attributes : []) {
        if (['href', 'src', 'poster'].includes(attr.name) && typeof attr.value === 'string') attr.value = withBase(attr.value);
      }
      for (const child of node.children || []) visit(child);
    };
    visit(tree);
  };
}
