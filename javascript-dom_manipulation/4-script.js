document.getElementById('add_item').addEventListener('click', function() {
  var newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('ul.my_list').appendChild(newItem);
});
