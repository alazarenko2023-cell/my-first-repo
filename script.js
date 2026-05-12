const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("keypress", function(e){

    if(e.key === "Enter"){

        let value = searchInput.value.toLowerCase();

        if(value.includes("1")){
            window.location.href = "pages/chapter1.html";
        }

        else if(value.includes("2")){
            window.location.href = "pages/chapter2.html";
        }

        else if(value.includes("3")){
            window.location.href = "pages/chapter3.html";
        }

        else if(value.includes("4")){
            window.location.href = "pages/chapter4.html";
        }

        else if(value.includes("5")){
            window.location.href = "pages/chapter5.html";
        }

        else{
            alert("Нічого не знайдено");
        }

    }

});