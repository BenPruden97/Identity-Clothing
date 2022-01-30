# IDENTITY CLOTHING

# TESTING FILE

# Table of Contents

* [Testing User Stories](#testing-user-stories)
* [Testing Project Functionality](#testing-project-functionality)
* [Testing Code Validation](#testing-code-validation)
* [Testing Lighthouse Performance](#testing-lighthouse-performance)

# Testing User Stories

### As a user, I would like to:

* View all clothing items available.
  * There are product categories for specific products and an all products page where all of the current products are listed.
* Have a search query, to find a specific clothing items.
  * There is a search page where users can enter a specific search query to find current products on the website. 
* Add items to my shopping cart that I would like to purchase.
  * On the product detail page, there is an add to cart button where the item will be added to the user's cart.
* Select clothing items for men.
  * There is a men's category page where only men's products display.
* Select clothing items for women.
  * There is a women's category page where only women's products display.
* Select clothing items that are currently on sale.
  * There is a item's on sale category page where only item's on sale products display.
* Select the size of my clothing item.
  * There is an option field with the following sizes available to users. XXS, XS, S, M, L, XL, XXL.
* Select the quantity of my clothing item.
  * There is a quantity field where users can select between a quantity of 1 or 99 for that clothing item.
* Sign-up for an account.
  * There is a sign up page where users are able to sign up for an account with Identity Clothing.
* Contact developer/ site owner if needed.
  * There is a contact page where users can submit a contact form for any help or advice. There is also a FAQ section for the most frequently asked questions.

### As a registered/ exisiting user, I would like to:

* Sign into my account.
  * There is a sign in page where registered users are able to sign into their account.
* View all of my previous orders to keep a record of my transaction.
  * Registered users can find their order history and previous order's information within their profile page.
* Be able to add & edit product reviews for products.
  * There is a product review section within the product detail page. In this page, registered users can add and edit their product reviews.
* Edit default information if any information needs to be updated.
  * Registered users can update their delivery and personal information within their profile page.
* View clothing items within my shopping cart.
  * Registered users are able to view all items that they have added to their shopping cart.
* Remove clothing items from my shopping cart if I no longer want them.
  * There is remove item link that will remove the item from the users shopping cart.
* Update a clothing item’s quantity within my shopping cart before purchasing.
  * There is an update item link that will update the quantity of the product within the shopping cart.
* Securely purchase any clothing items within my shopping bag.
  * After viewing their shopping cart, registered users can then proceed to checkout to purchase their shopping cart items.
* Receive an email for confirmation of my order.
  * After a successful purchase, the registered user will receive a confirmation of their order.

As a admin, I would like to:
* Sign into my admin account.
  * Admin users are able to sign into their admin account.
* Delete products that may need replacing or need to be removed from the website/ database.
  * Admin users are able to delete products and products on sale from the website.
* Add products to the website/ database.
  * Admin users are able to add products and products on sale to the website.
* Edit products on the website/ database.
  * Admin users are able to edit & update products and products on sale on the website.
* Delete member reviews if they are irrelevant to the product from the website/ database.
  * Only Admin users are able to remove product reviews from the website.
* Be able to shop and purchase clothing items like a regular user.
  * Admin users are able to use the Identity Clothing website just like any other user.

[Back To Table Of Contents](#table-of-contents)

# Testing Code Validation

### HTML Validation

Common errors/ warnings for all pages
  * Javascript tags - This was because of the Toast Messages JS to display for all pages
  * Empty Heading tags for <h5> - This was because of the average rating star icons to display the average rating for each product
  * Search Page - Stray end div tags from line 401 & 403. I was not able to located the stray end divs.
  * Contact Page - Accordion error. This was due to the FAQ looping for each accordion header and body templating
  * Sign Up Page - End Tag for body on line 497. Also an unclosed div element on line 261. both of these errors could not be found.
 
 Apart from these errors/ warnings listed. All pages passed the validation.

### CSS Validation

I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate my CSS style sheet.

base.css File

![Base CSS File]()

checkout.css File

![Checkout CSS File]()

profile.css File

![Profile CSS File]()

### JSHint Validation
 
JSHint was used to validation the Javascript across my project. The errors are listed below:
  * EmailJS & Swal - These are unused variables that are used for a success or error message after the user submits a contact form.
  * SwiperJS - This is an unused variable for the home page carousel that loops through products to display the most popular items.
  * Stripe - This is an unused variable for the stripe_elements.js file for Stripe Payments.
 
### Flake8 Validation
 
Some of the common errors for flake8 validation are listed below:
  * Lines too long - I updated most of the lines of code that were too long. There were some lines that could not be shortened.
  * Class has no object member - This was not needed
  * Variables not being used - Those variables were needed to view data within templates for looping and displaying content
 
[Back To Table Of Contents](#table-of-contents)

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

|Performance|Accessibility|Best Practice|SEO|Performance Issue|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|74|59|87|91|Bootstrap CSS & JS Links & Unused JS which is from Toast Messages|Due to the quantity input and ARIA IDs|

### Shopping Cart Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|94|68|100|91|Due to the quantity input and links|

### Shopping Cart Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|75|68|100|91|Bootstrap CSS & JS Links & Unused JS which is from Toast Messages|Due to the quantity input and ARIA IDs|

### Product Management Page Desktop Performance

|Performance|Accessibility|Best Practice|SEO|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|98|78|100|90|Due to the Select Image Input Field|

### Product Management Page Mobile Performance

|Performance|Accessibility|Best Practice|SEO|Performance Issue|Accessibility Issue|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
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
