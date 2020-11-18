# Card Maker

OmniGraffle template and script to generate cards from data.

Features:

- merge data property values with graphic's text
- style graphics based on a data property from visual style prototype
- export individual cards as individual files

## Installation and Requirements

Requires OmniGraffle version ≥ 7.18.

To install the script in OmniGraflle do the following steps:

1. open OmniGraffle
2. Select menu _Automation_ → _Configure…_
3. Select _Add Linked Folder_
4. Select the _CardMaker_ folder in this repository containing the scripting files.

## Creating Cards

1. Open the _CardMaker.graffle_ document
2. Select menu _Automation_ → _Create Cards_
3. Cards are generated in the sheet named `sheet`

You can export cards as PDFs or any other format individually:

1. Select the canvas named `sheet`
2. Menu _File_ → _Export…_ or `Cmd+Opt+E`
3. Chose your format: PNG, PDF, ...
5. Check ✅ _Export from artboards only_

This will generate one file per card with filename being the card's name.

## Template Document

The template document has a specific content. 

- Document MUST contain sheet named `template`
- Sheet named `template` MUST contain an object with name `card` and it MUST be a group
- Document MUST contain sheet named `card`. Content will be replaced
- Document MUST contain sheet named `sheet`. Content will be replaced.
    - Sheet named `sheet` must contain a layer layer named `sheet`
    - Sheet named `sheet` must contain an artboard layer named `artboard`

## Cards Data

Cards data are read from a JSON file. The JSON file is a dictionary. 

Keys:

- `cards`: array of cards represented as dictionaries

### Card

Card structure is left to the author of the template and the cards.
The following properties are expected by the provided template:

- `name` – card name/label
- `type` – card type
- `text` – card body text

# Card Template and Data Merging

Card template is stored in a sheet named `template`. It is a group of graphics that has name `card`.

## Card Template Properties

Card template graphic objects name denotes which field will be used as the graphic's text. For example, if the template has a text object with name `label` it will be replaced by value of card's property `label`.

Graphic's user data:

- `styleProperty` – name of card’s property that contains name of the style to be applied to the object (see more about styles below)

## Styles

Objects can be styled based on value of card's property. Style is specified by creating another object with that style. This approach makes it visually explicit how the styles look like instead of hiding it in an obscure textual representation.

The objects representing styles are objects in the canvas `template`. They are identified by having a user property `type` set to `style`. Their name denotes the style name.

### Styles Example

Cards have a property `type` that can be either `action` or `resource`. We want to have action cards to have a red border and resource cards to have a green border. We create two border-like templates: one red and one green. Canvas will have the following style objects:

- red rectangle with name `action` and `type` set to `style`
- green rectangle with name `resource` and `type` set to `style`

The card template would have a rectangle object with `styleProperty` set to `type`. It can be styled in some default style that will be used when the cards `type` contains unknown type or a type that is not to be styled differently.


# Authors

- Stefan Urbanek <stefan.urbanek@gmail.com>

# License

- Template: Attribution-ShareAlike 4.0 
- Code: MIT