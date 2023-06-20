const btn = document.querySelector("button")
const title = document.querySelector("h2")
const text = document.querySelector("p")
const date = document.querySelector("small")
const author = document.querySelector("h3")
const myUrl = "http://127.0.0.1:8000/article-list/"
let articles
let article

const getRandomElement = list => {
  return list[Math.floor(Math.random()*list.length)]
}

// function displayData(){
//   title.innerHTML = article.title
//   text.innerHTML= article.text
//   date.innerHTML= article.date.slice(0,10)
//   author.innerHTML= article.author
// }

async function getArticles(url) {
    const response = await fetch(url);
    const jsonData = await response.json();
    return jsonData
  }

getArticles(myUrl)
.then((data) => {
  articles = data.results
  btn.addEventListener("click", () => {
    article = getRandomElement(articles)
    title.innerHTML = article.title
    text.innerHTML= article.text
    date.innerHTML= article.date.slice(0,10)
    author.innerHTML= article.author
  })
})



