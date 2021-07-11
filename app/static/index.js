function deletecontact(contato){
    fetch('/delete-contact',{
        method: 'POST',
        body: JSON.stringify({ contato: contato })
    }).then((_res) => {
        window.location.href = "/home";
    });
}

function updatecontact(contato){
    fetch('/update',{
        method: 'POST',
        body: JSON.stringify({ contato: contato })
    }).then((_res) => {
        window.location.href = "/atualizar";
    });
}