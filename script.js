// Optional: Click to show which item was clicked
document.querySelectorAll('.menu-item').forEach(item => {
  item.addEventListener('click', () => {
    alert("You selected: " + item.querySelector('h4').textContent);
  });
});
