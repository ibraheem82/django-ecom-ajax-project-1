let btns = document.getElementsByClassName('addtocart')
for(let i = 0; i < btns.length; i++){
  btns[i].addEventListener('click', function(e){
    let product_id = e.target.dataset.product
    let action = e.target.dataset.action
    console.log(product_id)
    if(user=='AnonymousUser'){
      console.log('Ypu are not signed in')
    }

    else{
      addToCart(product_id, action)
    }
  })
}


function addToCart(p_id, act){
  const data = {product_id: p_id, action: act};


let url = '/updatecart'
fetch(url, {
  method: 'POST', // or 'PUT'
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken
  },
  body: JSON.stringify(data),
})
.then(response => response.json())

.then(data => {
  console.log('Success:', data);
  // Display an alert when item is added
  alert('Item added to the cart');


  
      // Create and append the success alert
      const alertContainer = document.getElementById('alert-container');
      console.log('Alert Container:', alertContainer);

      const successAlert = document.createElement('div');
      successAlert.classList.add('alert', 'alert-success', 'd-flex', 'align-items-center');
      successAlert.setAttribute('role', 'alert');
      successAlert.innerHTML = `
        <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Success:">
          <use xlink:href="#check-circle-fill"/>
        </svg>
        <div>
          Cart updated successfully
        </div>
      `;

      // Append the alert to the container
      alertContainer.innerHTML = '';
      alertContainer.appendChild(successAlert);
  document.getElementById('cart').innerHTML = `<h4>${data.quantity}</h4>`
})
.catch((error) => {
  console.error('Error:', error);
});

}

let inputfields = document.getElementsByTagName('input')
for(let i =0; i<inputfields.length; i++){
  inputfields[i].addEventListener('change', updateQuantity)
  
}

// function updateQuantity(e){
//   let inputvalue = e.target.value
//   let product_id = e.target.dataset.product

//   const data = {p_id: product_id, in_val: inputvalue};
// let url = '/updatequantity'

//   fetch(url, {
//     method: 'POST', // or 'PUT'
//     headers: {
//       'Content-Type': 'application/json',
//       'X-CSRFToken': csrftoken
//     },
//     body: JSON.stringify(data),
//   })
//   .then(response => response.json())
//   .then(data => {
//     console.log('Success:', data);
//     e.target.parentElement.parentElement.children[4].innerHTML = `<h3>$${data.subtotal.toFixed(2)}</h3>`
//     document.getElementById('total').innerHTML = `<h3><strong>$${data.grandtotal.toFixed(2)}</strong></h3> `
//     document.getElementById('cart').innerHTML = `<h4>${data.quantity}</h4>`
    
//   })
//   .catch((error) => {
//     console.error('Error:', error);
//   });
// }