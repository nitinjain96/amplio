function showSidebar() {
    $('.ui.sidebar').sidebar('toggle');
}

function goTo(url) {
    window.location = url;
}

function toggleVisibility(button, field_identifier) {
    var $field = $('#' + field_identifier);
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

function initializePopups(string) {
    $(string).popup({inline: true});
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // These HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function setUpAjax() {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
}

function vote(div, url) {
    var $div = $(div);
    var feedback_id = parseInt($div.attr('data-feedback-id'));
    $.post(
        url,
        {id: feedback_id},
        function (data) {
            $('#votes-' + feedback_id).html(data);
        }
    );
    var $span = $div.find('span');
    if ($span.attr('data-voted') === 'true') {
        $div.html('<span class="fa fa-heart-o" data-voted="false"></span>');
    } else {
        $div.html('<span class="fa fa-heart" data-voted="true"></span>');
    }
    
}

function removeImage(url, reload) {
    $.post(
        url,
        {},
        function (data) {
            if (data === 'OK') {
                goTo(reload);
            } else {
                console.log('OK was not returned');
            }
        }
    )
}