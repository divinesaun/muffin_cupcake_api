document.addEventListener('DOMContentLoaded', () => {
    const postForm = document.getElementById('postForm');
    const formMessage = document.getElementById('formMessage');
  
    // Listen for form submission
    postForm.addEventListener('submit', (event) => {
      event.preventDefault();  // Prevent default form submission behavior
  
      // Capture form data
      const flour = parseInt(document.getElementById('flour').value.trim());
      const milk = parseInt(document.getElementById('milk').value.trim());
      const sugar = parseInt(document.getElementById('sugar').value.trim());
      const butter = parseInt(document.getElementById('butter').value.trim());
      const egg = parseInt(document.getElementById('egg').value.trim());
      const baking_powder = parseInt(document.getElementById('baking_powder').value.trim());
      const vanilla = parseInt(document.getElementById('vanilla').value.trim());
      const salt = parseInt(document.getElementById('salt').value.trim());
      // Clear any existing messages
      formMessage.textContent = '';
  
  
      // Prepare data to send (as a JSON object)
      const postData = {
        "Flour": flour,
        "Milk": milk,
        "Sugar": sugar,
        "Butter": butter,
        "Egg": egg,
        "Baking_Powder": baking_powder,
        "Vanilla": vanilla,
        "Salt": salt
      };
 
      // Send POST request to the local API endpoint
      fetch('/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
      })
      .then(response => {
        if (!response.ok) {
          throw new Error(`Server responded with status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
          formMessage.innerHTML = `${data.prediction}`;
          formMessage.style.color = 'white';
          // Optionally, reset the form after a successful post
          postForm.reset();
      })
      .catch(error => {
        // Display error message
        formMessage.textContent = `Error submitting post: ${error.message}`;
        formMessage.style.color = 'red';
      });
  });
});