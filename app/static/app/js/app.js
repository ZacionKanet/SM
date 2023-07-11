const nombre = document.getElementById("nombre");
const mail = document.getElementById("mail");
const Password = document.getElementById("Password");
const form = document.getElementById("form");
const warning = document.getElementById("warning");

form.addEventListener("submt", e=>{
    e.preventDefaul()
    let warning = ""
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    let entrar = false
    parrafo.innerHTML = ""
    if(nombre.value.lenght <3 ){
        warning += "nombre muy corto <Br>"
    }
    console.log(regexEmail.test(email.value))
    if(regexEmail.test(email.value)){
        warning += "El email no es valido <Br>"
    }
    if(Password.value.lenght <8){
        warning += "El Password debe tener al menos 8 caracteres <Br>"
    }
    if(entrar){
        parrafo.innerHTML = warning
    }
    if(entrar){
        parrafo.innerHTML = enviado
    }
})