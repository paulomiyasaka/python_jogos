$('input[type="file"').change(event => {
    
    let arquivos = event.target.files;
    
    if(arquivos.length > 0){
        if(arquivos[0].type == "image/jpeg"){
            //alert('aqui');
            $('img').remove();
            let imagem = $('<img class="figure-img img-fluid rounded">');
            imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
            $('figure').prepend(imagem);
        }
    }else{
        console.log('Sem imagem.');
    }

});