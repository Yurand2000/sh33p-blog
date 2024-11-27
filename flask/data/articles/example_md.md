## Headings
---

# h1 Heading
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading
p Text

Fuga sit inventore quaerat et placeat. Id odio qui sit deleniti. Maxime animi veniam magni omnis. Dolore dolorem nisi nobis. Itaque earum consequatur optio quia harum necessitatibus. Amet alias repellendus quisquam nihil.

Tempora ab et sunt dignissimos et sit. Non quia qui distinctio hic. Dolore voluptatibus quis impedit.

Non dolor et consequatur commodi aut repellendus. Explicabo necessitatibus laborum quod eum laborum quia rerum. Blanditiis quia ut distinctio. Quidem qui iure voluptatem est quas hic. Nesciunt qui id quasi reiciendis atque aliquam similique qui.

Veniam veniam laborum officia. Quaerat aliquam necessitatibus corporis eveniet dicta. Excepturi dolorum et totam aliquam quo sit dolorem. Repellendus et repudiandae veniam esse consequatur.

Nobis aut in voluptas ut. Qui sunt quia rerum magni repudiandae ut maiores. Nemo nobis in officia quaerat tenetur. Odit labore ullam soluta eligendi rerum. Aut repudiandae quia temporibus. Neque facilis id occaecati quis excepturi.

<br>
## Horizontal Rulers
---

\* Rulers start

___

---

***

\* Rulers end

<br>
## Emphasis
---

**This is bold text** or __this is other bold text__

*This is italic text* or _this is other italic text_

<br>
## Blockquotes
---

> Quoting time

Break with text or explicit `<br>` tag

> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.

<br>
## Lists
---

### Unordered

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

### Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

<br>
## Code
---

Inline `code`

Indented code for blocks

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code

<br>
## Tables
---

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

Center aligned columns

| Option | Description |
|:------:|:-----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

Right aligned columns

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

Tables inside HTML

<div class="flex flex-col items-center" markdown="1">
| Option | Description |
|:------:|:-----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
</div>

<div class="flex flex-col w-full" markdown="1">
| Option | Description |
|:------:|:-----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
</div>

<br>
## Links
---

[link text](/)

<br>
## Raw HTML
---

#### Non preprocessed HTML

<p class="text-md pb-2 text-red-500 font-bold">This HTML is not preprocessed</p>

#### Markdown inside HTML

<div class="mx-auto text-center" markdown="1">
`<div class="mx-auto text-center" markdown="1">`

###### h6 heading

paragraph with markdown parsed text ([link text](/))

</div>

<br>
## Images
---

Best to use raw html as you can set image sizes and other attributes.

<img class="mx-auto rounded-lg" src="/static/sheeps.jpg" width="400"/>

<br>
## Footnotes
---

Footnote referencing[^footnote_name]

[^footnote_name]: Footnote