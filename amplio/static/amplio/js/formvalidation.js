$('#sign-in').form({
    fields: {
        email: {
            identifier: 'email',
            rules: [
                {
                    type: 'empty',
                    prompt: 'Please enter your email address'
                },
                {
                    type: 'email',
                    prompt: 'Please enter a valid email address'
                }
            ]
        },
        password: {
            identifier: 'password',
            rules: [
                {
                    type: 'empty',
                    prompt: 'Please enter your password'
                }
            ]
        }
    }
});

$('#sign-up').form({
    fields: {
        name: {
            identifier: 'name',
            rules: [
                {
                    type: 'empty',
                    prompt: 'Please enter your name'
                }
            ]
        },
        email: {
            identifier: 'email',
            rules: [
                {
                    type: 'empty',
                    prompt: 'Please enter your email address'
                },
                {
                    type: 'email',
                    prompt: 'Please enter a valid email address'
                }
            ]
        },
        password: {
            identifier: 'password',
            rules: [
                {
                    type: 'empty',
                    prompt: 'Please choose a password'
                },
                {
                    type: 'minLength[8]',
                    prompt: 'Your password must be at least {ruleValue} characters long'
                }
            ]
        }
    }
});