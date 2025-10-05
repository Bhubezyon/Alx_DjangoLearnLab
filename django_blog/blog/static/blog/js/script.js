// blog/static/blog/js/script.js
console.log("Blog JS loaded - script.js:2");

AuthenticatorAssertionResponse.apply(this, arguments);
console.log("Blog JS loaded - script.js:5");

// If you want to inject this CSS via JavaScript, use the following:
const style = document.createElement('style');
style.textContent = `
.auth-form {
    max-width: 300px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}
`;
document.head.appendChild(style);