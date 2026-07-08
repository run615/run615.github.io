import rss from '@astrojs/rss';

export async function GET(context) {
  const { getCollection } = await import('astro:content');
  const posts = await getCollection('blog');
  return rss({
    title: 'run615',
    description: 'run615 的个人博客',
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: new Date(post.data.pubDate),
      link: `/blog/${post.id}/`,
    })),
  });
}
