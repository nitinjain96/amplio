function showSidebar() {
    $('.ui.sidebar').sidebar('toggle');
}

function goTo(url) {
    window.location = url;
}

function toggleVisibility(button, field_identifier) {
    var $field = $('#'+field_identifier);
    if ($field.attr('type') === 'password') {
        $field.attr('type', 'text');
        button.innerHTML = '<span class="fa fa-eye-slash"></span>';
    } else {
        $field.attr('type', 'password');
        button.innerHTML = '<span class="fa fa-eye"></span>';
    }
}

function initializeDropdowns() {
    $('.ui.dropdown').dropdown();
}