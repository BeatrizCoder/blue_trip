let inputDestino = document.querySelector('#destino')
let inputImagem = document.querySelector('#imagem')
let inputPreco = document.querySelector('#preco')
let textareaDescricao = document.querySelector('#descricao')
let inputbtn = document.querySelector('#cadastro')
let nomeOk = false 
let emailOk = false 
let msgOk = false

btnEnviar.disabled = true



// CAMPO DO DESTINO
inputDestino.addEventListener('keydown', () => { 

    if(inputDestino.value.length < 4){
       inputDestino.style.borderColor = 'red' 
       nomeOk = false
    } else {
       inputDestino.style.borderColor = 'blue' 
       DestinoOk = true
    }
 
    if(inputDestino.value == '' || inputNome.value == undefined || inputNome.value == null) {
       inputDestino.style.borderColor = '#ccc'
    }
 

    if (nomeOk && emailOk && msgOk) {
       btnEnviar.disabled = false
    } else { 
       btnEnviar.disabled = true
    }
 
 })

//  CAMPO DA IMAGEM
 inputImagem.addEventListener('keydown', () => { 

    if(inputImagem.value.length < 4){
        inputImagem.style.borderColor = 'red' 
       nomeOk = false
    } else {
        inputImagem.style.borderColor = 'blue' 
       DestinoOk = true
    }
 
    if(inputImagem.value == '' || inputImagem.value == undefined || inputImagem.value == null) {
        inputImagem.style.borderColor = '#ccc'
    }
 

    if (nomeOk && emailOk && msgOk) {
       btnEnviar.disabled = false
    } else { 
       btnEnviar.disabled = true
    }
 
 })

//  CAMPO DE DESCRICAO
textareaDescricao.addEventListener('keydown', () => { 

    if(textareaDescricao.value.length < 4){
        textareaDescricao.style.borderColor = 'red' 
       nomeOk = false
    } else {
        textareaDescricao.style.borderColor = 'blue' 
       DestinoOk = true
    }
 
    if(textareaDescricao.value == '' || textareaDescricao.value == undefined || textareaDescricao.value == null) {
        textareaDescricao.style.borderColor = '#ccc'
    }
 

    if (nomeOk && emailOk && msgOk) {
       btnEnviar.disabled = false
    } else { 
       btnEnviar.disabled = true
    }
 
 })





// CAMPO DO PRECO
inputPreco.addEventListener('keydown', () => { 
    if(inputNome.value.length < 4){
       inputNome.style.borderColor = 'red' 
    } else {
       inputNome.style.borderColor = 'blue'
    }
 })

 













 textareaDescricao.addEventListener('keyup', ()=>{
    if(textareaDescricao.value.length > 100){
       textareaDescricao.style.borderColor = 'red' 
    } else {
       textareaDescricao.style.borderColor = 'green' 
    }
 })
 





 
btnEnviar.addEventListener('click', () => {
    alert('Mensagem enviada com sucesso!, aguarde pelo retorno ;D')
 })
 
 audi