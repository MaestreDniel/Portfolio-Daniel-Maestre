---
title: Components
layout: layout.html
eleventyNavigation:
  key: Components
  order: 2
---

# Components

I have different types of components that help to the maintainability of my code.

Check the list of components to get more information:

{% assign navPages = collections.all | eleventyNavigation: "Components" %}
{{ navPages | eleventyNavigationToHtml }}