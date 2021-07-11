function deletecontact(contato){
    fetch('/delete-contact',{
        method: 'POST',
        body: JSON.stringify({ contato: contato })
    }).then((_res) => {
        window.location.href = "/home";
    });
}