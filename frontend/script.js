
const API = "http://localhost:8000/mangas";


// barcha manga olish

async function getMangas(){

    const response = await fetch(`${API}/`);

    const mangas = await response.json();

    showMangas(mangas);

}



function showMangas(mangas){

    const container =
    document.getElementById("mangaContainer");


    container.innerHTML="";


    mangas.forEach(manga=>{


        container.innerHTML += `

        <div class="card">

            <h2>${manga.title}</h2>

            <p>
            ${manga.description ?? ""}
            </p>

            <p>
            Genre:
            ${manga.genre}
            </p>


            <button onclick="getChapters(${manga.id})">
            Chapters
            </button>

        </div>

        `;


    });


}



// search endpoint

async function searchManga(){


    const query =
    document.getElementById("searchInput").value;


    const response =
    await fetch(`${API}/search?query=${query}`);


    const data =
    await response.json();


    showMangas(data);


}



// genre endpoint

async function filterGenre(){


    const genre =
    document.getElementById("genreInput").value;


    const response =
    await fetch(`${API}/genre?genre=${genre}`);


    const data =
    await response.json();


    showMangas(data);


}



// chapters olish

async function getChapters(id){


    const response =
    await fetch(`${API}/${id}/chapters`);


    const chapters =
    await response.json();


    const container =
    document.getElementById("chapterContainer");


    container.innerHTML="";


    chapters.forEach(chapter=>{


        container.innerHTML += `

        <div class="chapter">

        <h3>
        Chapter ${chapter.number}
        </h3>


        <button onclick="
        openChapter(${id},${chapter.id})
        ">
        Read
        </button>

        </div>

        `;


    });


}




// bitta chapter

async function openChapter(mangaId, chapterId){


    const response =
    await fetch(
    `${API}/${mangaId}/chapters/${chapterId}`
    );


    const chapter =
    await response.json();


    alert(
    JSON.stringify(chapter,null,2)
    );


}




getMangas();