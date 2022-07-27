# Book Cover API

Simply put in a title of a book and it's author to receive a link to the book cover.

## Example Link

```
https://book-coverapi.herokuapp.com/get?title=Lord+of+the+Rings&author=j.r.r+tolkien
```

## JavaScript usage example
```js
function formatForURL(string) {
  let result = string.toLowerCase().split(" ").join("+");
  return result;
}

async function getImgURL(title, author) {
  let bookTitle = formatForURL(title);
  let bookAuthor = formatForURL(author);
  let response = await fetch(
    `https://book-coverapi.herokuapp.com/get?title=${bookTitle}&author=${bookAuthor}`,
    {
      method: "GET",
      mode: "cors",
    }
  ).catch((err) => {
    alert(title + " image could not be found");
  });
   
  await response.json().then((data) => {
      let img = document.createElement("img");
      img.src = data;
  });
  
}
```