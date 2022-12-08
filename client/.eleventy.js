const markdownIt = require("markdown-it");
const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const pluginMermaid = require("@kevingimbel/eleventy-plugin-mermaid");
const eleventyNavigationPlugin = require("@11ty/eleventy-navigation");

module.exports = function(eleventyConfig) {
  // Plugins for syntax highlighting and mermaid
  eleventyConfig.addPlugin(syntaxHighlight);
  eleventyConfig.addPlugin(pluginMermaid);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);

  // Set markdownIt config
  eleventyConfig.setLibrary(
    "md",
    markdownIt({
      html: true,
      breaks: true,
      linkify: true
    })
  );

  eleventyConfig.addPassthroughCopy("src/assets/images/docs");

  // Create a "docs" collection from all the markdown files
  eleventyConfig.addCollection("docs", collection => {
    const _collection = collection.getFilteredByGlob("**/*.md")
    return _collection;
  });

  return {
    dir: {
      includes: "eleventy/_includes", // where the root file is
      input: ".", //all files but we just use markdown
      output: "docs" //output directory
    }
  };
};
