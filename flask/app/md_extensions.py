from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

class TailwindExtension(Extension):
    """An extension to add classes to tags"""

    def extendMarkdown(self, md):
        md.treeprocessors.register(
            TailwindTreeProcessor(md), "tailwind", 20)


class TailwindTreeProcessor(Treeprocessor):
    """Walk the root node and modify any discovered tag"""

    classes = {
        # general text
        "h1" : "text-4xl pb-2 font-extrabold text-gray-900 dark:text-white",
        "h2" : "text-3xl pb-2 font-bold text-gray-900 dark:text-white",
        "h3" : "text-2xl pb-2 font-bold text-gray-900 dark:text-white",
        "h4" : "text-xl pb-2 font-bold text-gray-900 dark:text-white",
        "h5" : "text-lg pb-2 font-bold text-gray-900 dark:text-white",
        "h6" : "text-md pb-2 font-bold text-gray-900 dark:text-white",
        "a"  : "underline dark:text-dark-200 dark:hover:text-dark-100",
        "p"  : "text-md pb-2 text-gray-900 dark:text-white",
        "sup": "p-1",

        # rulers
        "hr" : "h-px mb-2 bg-gray-200 border-0 bg-dark-800 dark:bg-dark-200",

        # lists
        "ul" : "max-w-md ml-4 space-y-1 text-dark-900 list-disc list-inside dark:text-dark-50",
        "ol" : "max-w-md ml-4 space-y-1 text-dark-900 list-decimal list-inside dark:text-dark-50",

        # block quotes
        "blockquote" : "mx-2 px-1 pt-2 py-1 mb-2 border-s-4 border-dark-300 bg-gray-50 dark:border-dark-500 dark:bg-dark-800",

        # code blocks
        "pre" : "font-mono m-2 p-2 pl-3 rounded-xl border-dark-300 bg-gray-50 dark:bg-dark-950 text-dark-800 dark:text-white",
        "code" : "font-mono rounded-md bg-gray-50 dark:bg-dark-950",

        # tables
        "table" : "text-left my-2",
        "thead" : "bg-dark-100 dark:bg-dark-800",
        "tbody" : "bg-white dark:bg-dark-950",
        "tr": "",
        "th": "text-sm uppercase p-1 font-bold text-dark-900 dark:text-white border dark:border-dark-500 ",
        "td": "text-sm p-1 text-gray-900 dark:text-dark-50 border dark:border-dark-500",
    }

    div_on_attribute = {
        "footnote": "mt-10 pt-2 px-2 rounded-b-2xl bg-dark-100 dark:bg-dark-800",
    }

    def run(self, root):
        for node in root.iter():
            if node.tag == "div" and "class" in node.attrib:
                for cl in node.attrib["class"].split():
                    tag_classes = self.div_on_attribute.get(cl)
                    if tag_classes:
                        node.attrib["class"] = tag_classes
            else:
                tag_classes = self.classes.get(node.tag)
                if tag_classes:
                    node.attrib["class"] = tag_classes
