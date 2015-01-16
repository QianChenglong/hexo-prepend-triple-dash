# hexo-prepend-triple-dash

Because the hexo ignore triple-dash of yaml fornt matter in  `scaffolds/post.md)`, like this

```
---
title: {{ title }}
categories: []
tags: []
date: {{ date }}
---
```

When I hexo new title.md, it generates like this

Become

```
title: title
categories: []
tags: []
date: 2015-01-15 17:32:51
---
```

I had raied an [Issue](https://github.com/hexojs/hexo/issues/993).

# usage

copy 'prepend.py' to your source directory(`_post/`), double click

# todo

Modify `hexo` source to fix this problem.
