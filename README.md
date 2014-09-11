Humanization
============

This repository is a collection of educational and background content for general use in any genomics context at the Broad Institute. 
It contains a bunch of small *snippets* of up to a few sentences explaining a particular term or concept. 

For example, the snippet for *Exome Capture* is: 

[TODO]

On the genomics platform QC portal, there is a question mark help icon next to the word *exome capture*, 
and this is displayed when you hover over it. The content is pulled directly from here! 

This is primarily used in internal web *portals*, but in principle it could be included anywhere, 
such as an online textbook or a command line application. 

## Contact 

This repository is informally managed by Mary Carmichael (maryc@broadinstitute.org). 
She can answer questions about specific content or use cases. 

The first version of this repo was prototyped quickly by Mary and Brett Thomas (brett@movegenomics.com). 
At some point, we will likely migrate the content into a more fully featured CMS and deprecate this repo. 
Feel free to contact Mary if you might want to collaborate on that. 

## Content Organization

Snippets are written in **Markdown**, a simple format for writing rich text. 
The markdown compiles to HTML which can be embedded into any web app. 

Each snippet is in its own file, within the `content/` directory. 
Snippets are organized in directories, which is used for namespacing. 

For example, the **identifier** for the Exome Capture snippet is `ngs.exome_capture`. 
This means the content for this snippet is in `snippets/ngs/exome_capture.md`. 

In the QC portal, we include that content (as compiled HTML, not Markdown) with the tag `{% humanization 'ngs.exome_capture' %}` 
(Though note that the specific method for including content will vary across portals.) 

#### Some notes on the actual content 

- Links, bold, italic, etc. are allowed and encouraged - makes it much easier to read 

- Whitespace doesn't matter; don't worry about keeping the actual text files pretty. 

- You can use paragraphs - just put an empty line between text

- I don't think we should use headers here. 

- *Please let me know if there's anything you want to do but can't - I'm really flexible!* 

## Install 

For now, just have Brett install this on your computer. 
This is a simple Python/Flask app, but it requires a few pypi packages. 

## Running

To run the **local server**, open up *Terminal* and type `source ~/run_content.sh`. 

Then go to http://localhost:5000 in your web browser, and it should be there. 

As you make changes to the content, they will show up in the browser. 

## TODO

- should we allow images?

- should you be able to link from one snippet to another?

- brett needs to write up more about the technical details of how this works 

- does mary want to post this publicly for others to see the database of content? 
