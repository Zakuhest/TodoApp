console.log("Hola a todos, soy Javascript");

function edit(){
    this.innerHTML = 'Cancelar';
    const spanText = document.querySelector('#taskText');
    const taskText = spanText.innerText;

    const inputText =  '<input type="text" id="inputText" class="form-control d-inline" placeholder='+taskText+'></input>';
    const btnSave = '<a href="javascript: save();" class="btn btn-primary">Guardar</a>';
    spanText.innerHTML += inputText + btnSave;

    console.log("editando...")
}

function save(){
    const id = document.querySelector("#taskId").innerText;
    const text = document.querySelector('#inputText').value;
    console.log(text)

    const formData = new FormData();
    formData.append('id', id)
    formData.append('text', text)

    //XHR: PUT
    fetch("/update/"+id,{
        method: "PUT",
        body: formData
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
}