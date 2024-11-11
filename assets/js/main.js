function obtenerDatosTarea(grilla_id) {
    // Realiza la solicitud AJAX
    fetch(`/${grilla_id}/grilla`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error("Error:", data.error);
        } else {
            console.log("Datos de la tarea:", data);
            classList.add()
            
            // Aquí puedes manipular los datos recibidos
        }
    })
    .catch(error => {
        console.error("Error en la solicitud:", error);
    });
}


obtenerDatosTarea