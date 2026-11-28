const API = "http://127.0.0.1:8000/mangas";



// =======================
// LOAD ALL MANGAS
// =======================

async function loadMangas(){


    const response = await fetch(`${API}/`);


    const mangas = await response.json();


    displayMangas(mangas);

}




// =======================
// DISPLAY CARDS
// =======================


function displayMangas(mangas){


    const container =
    document.getElementById("mangaContainer");


    container.innerHTML="";



    mangas.forEach(manga=>{


        const card =
        document.createElement("div");


        card.className="manga-card";



        card.innerHTML=`

        <h2>${manga.title}</h2>

        <p>
        Author: ${manga.author}
        </p>


        <p>
        Chapters: ${manga.chapters}
        </p>


        <button onclick="getManga(${manga.id})">
        Details
        </button>


        <button onclick="deleteManga(${manga.id})">
        Delete
        </button>


        `;



        container.appendChild(card);


    });


}





// =======================
// GET ONE MANGA
// =======================


async function getManga(id){


    const response =
    await fetch(`${API}/${id}`);



    const manga =
    await response.json();



    document.getElementById(
        "mangaDetails"
    ).innerHTML=`


    <h2>${manga.title}</h2>


    <p>
    Author:
    ${manga.author}
    </p>


    <p>
    ${manga.description}
    </p>


    <p>
    Chapters:
    ${manga.chapters}
    </p>


    `;


}






// =======================
// SEARCH
// =======================


async function searchManga(){


const query =
document.getElementById(
"searchInput"
).value;



const response =
await fetch(
`${API}/search?query=${query}`
);



const mangas =
await response.json();



displayMangas(mangas);


}






// =======================
// GENRE FILTER
// =======================


async function filterGenre(){


const genre =
document.getElementById(
"genreInput"
).value;



const response =
await fetch(
`${API}/genre?genre=${genre}`
);



const mangas =
await response.json();



displayMangas(mangas);


}






// =======================
// ADD MANGA
// =======================


async function addManga(){



const manga={


title:
document.getElementById(
"titleInput"
).value,


author:
document.getElementById(
"authorInput"
).value,


description:
document.getElementById(
"descriptionInput"
).value,


chapters:Number(
document.getElementById(
"chaptersInput"
).value
)



};



const response =
await fetch(
`${API}/`,
{

method:"POST",


headers:{
"Content-Type":"application/json"
},


body:
JSON.stringify(manga)

}

);



if(response.ok){

alert(
"Manga added"
);


loadMangas();

}


}






// =======================
// DELETE
// =======================


async function deleteManga(id){


await fetch(
`${API}/${id}`,
{
method:"DELETE"
}
);



loadMangas();


}







// =======================
// START
// =======================


loadMangas();