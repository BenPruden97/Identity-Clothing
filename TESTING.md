# IDENTITY CLOTHING

# TESTING FILE

# Table of Contents

* [Testing User Stories](#testing-user-stories)
* [Testing Project Functionality](#testing-project-functionality)
* [Testing Code Validation](#testing-code-validation)
* [Testing Lighthouse Performance](#testing-lighthouse-performance)

# Testing Lighthouse Performance

### Home Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|97|94|100|91|

### Home Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|70|94|93|92|Images in next gen format & HTTP/2|

### Search Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|98|90|100|90|

### Search Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|74|90|100|92|Bootstrap CSS & JS Links & Unused JS which is for Toast Messages|

### Contact Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|88|93|100|90|Bootstrap CSS & JS Links & Unused JS which is for Toast Messages|

### Contact Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|72|93|100|92|Bootstrap CSS & JS Links & Unused JS which is for Toast Messages|

### Sign Up Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|98|90|100|90|

### Sign Up Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|75|90|100|90|Bootstrap CSS & JS Links & Unused JS which is for Toast Messages|

### Sign In Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|98|90|100|90|

### Sign In Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|76|90|100|92|Bootstrap CSS & JS Links & Unused JS which is for Toast Messages|

### Men's Products Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|97|89|100|91|

### Men's Products Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|73|89|93|92|Images in next gen format & HTTP/2|

### Women's Products Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|97|89|100|91|

### Women's Products Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|71|89|93|92|Images in next gen format & HTTP/2|

### Item's on Sale Products Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|97|89|100|91|

### Item's on Sale Products Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|74|89|93|92|Images in next gen format & HTTP/2|

### All Products Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|96|89|100|91|

### All Products Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|66|89|93|92|Images in next gen format & HTTP/2|

### Product Detail Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|98|59|87|91|Due to the quantity input and ARIA IDs

### Product Detail Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|74|59|87|91|Bootstrap CSS & JS Links & Unused JS which is from Toast Messages|Due to the quantity input and ARIA IDs|

### Shopping Cart Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|94|68|100|91|Due to the quantity input and links|

### Shopping Cart Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|75|68|100|91|Bootstrap CSS & JS Links & Unused JS which is from Toast Messages|Due to the quantity input and ARIA IDs|

### Product Management Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|98|78|100|90|Due to the Select Image Input Field|

### Product Management Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|75|78|100|90|Bootstrap CSS & JS Links & Unused JS which is from Toast Messages|Due to the Select Image Input Field|

### Profile Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|97|90|100|90|

### Profile Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|75|90|100|92|Bootstrap CSS & JS Links & Unused JS which is from Toast Messages|

### Checkout Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|98|91|100|91|

### Checkout Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|74|91|100|92|Bootstrap CSS & JS Links & Unused JS which is from Toast Messages|

### Order Confirmation Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|
|:-----:|:-----:|:-----:|:-----:|
|97|93|100|90|

### Order Confirmation Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|75|93|100|92|Bootstrap CSS & JS Links & Unused JS which is from Toast Messages|

Common Issues to note:

Images in next gen formats & HTTP/2
  * This issues is for the amount of images on a page and the format. The HTTP/2 requires additional support for functionality.

Bootstrap CSS & JS Links & Unused JS which is from Toast Messages
  * This issue is mostly on mobile devices and is from the Bootstrap CSS & JS Links.
  * The unused JS is also from the toast message & back to top button js for all pages. Both of these issues could not be changed.

Due to the quantity input and links
  * This issue is for the quantity input field and decrement, increment buttons and their ARIA IDs. This could not be changed.
  
Due to the select image input
  * This issue is for the image input field to add an image to a product. This could not be changed.

[Back To Table Of Contents](#table-of-contents)
