const countries = ["Egypt", "Estonia", "Ethiopia", "England", "El Salvador", "Ecuador", "France", "Germany", "Greece", "India", "Italy", "Japan"];

    // Populate the country dropdown with search functionality
    const countrySelect = document.getElementById('country');
    countries.forEach(country => {
        const option = document.createElement('option');
        option.value = country;
        option.text = country;
        countrySelect.add(option);
    });

    // Sign Up Form Validation
    const signupForm = document.getElementById('signup-form');
    signupForm.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent form submission for validation
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // Email Validation (Check if it contains @)
        if (!email.includes('@')) {
            alert('Invalid email address.');
            return;
        }

        // Password Validation (Check for both letters and numbers)
        const hasLetters = /[a-zA-Z]/.test(password);
        const hasNumbers = /[0-9]/.test(password);

        if (!hasLetters || !hasNumbers) {
            alert('Password must contain both letters and numbers.');
            return;
        }

        alert('Sign Up Successful!');
    });

    // Sign In Form Submission (Just a placeholder action)
    const signinForm = document.getElementById('signin-form');
    signinForm.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent actual submission
        alert('Sign In Successful!');
    });
