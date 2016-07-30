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

function vote(div) {
    var $div = $(div);
    var feedback_id = parseInt($div.attr('data-feedback-id'));
    $.post(
        'amplio/vote',
        {id: feedback_id},
        function (data) {
            $('#votes-' + feedback_id).html(data);
        }
    );
    var $span = $div.find('span');
    if ($span.attr('data-voted') === 'true') {
        $div.html('<span class="fa fa-heart-o" data-voted="false"></span>');
    } else {
        $div.html('<span class="red-text fa fa-heart" data-voted="true"></span>');
    }
}

function subscribe(a) {
    var $a = $(a);
    var comment_id = parseInt($a.attr('data-comment-id'));
    $.post(
        'amplio/subscribe',
        {id: comment_id},
        function (data) {
            $('#subscribers-' + comment_id).html(data);
        }
    );
    var $span = $a.find('span');
    if ($span.attr('data-subscribed') === 'true') {
        $a.html('<span class="fa fa-thumbs-o-up" data-subscribed="false"></span>');
    } else {
        $a.html('<span class="blue-text fa fa-thumbs-up" data-subscribed="true"></span>');
    }
    event.preventDefault();
}

function showReplyForm(a, user_email) {
    var $a = $(a);
    var comment_id = $a.attr('data-comment-id');
    var feedback_id = $a.attr('data-feedback-id');
    $a.hide();
    var $content = $('#content-' + comment_id);
    var form_text = '' +
        '<form id="form-' + comment_id + '" class="ui reply form">\n' +
        '    <div class="field">\n' +
        '       <label>Reply:</label>\n' +
        '       <input type="text" placeholder="Reply">\n' +
        '   </div>\n' +
        '   <button type="submit" \n' +
        '           class="ui primary button"\n' +
        '           onclick="submitReply(' + '\'' + user_email + '\', ' + feedback_id + ', ' + comment_id + ')">\n' +
        '       <span class="fa fa-comments-o"></span>&nbsp;&nbsp;&nbsp;Reply\n' +
        '   </button>\n' +
        '</form>';
    $content.html($content.html() + form_text);
    event.preventDefault();
}

function submitReply(user_email, feedback_id, comment_id) {
    var $form = $('#form-' + comment_id);
    var $input = $form.find('input');
    var text = $input.val();
    $.post(
        '/amplio/reply/',
        {
            user_email: user_email,
            upon_feedback: feedback_id,
            upon_comment: comment_id,
            text: text
        },
        function (data) {
            if (data === 'OK') {
                location.reload(true);
            } else {
                console.log('OK was not returned');
            }
        }
    );
}

function submitTierOne(user_email, feedback_id) {
    var $form = $('#tier-one-comment-form');
    var $input = $form.find('input');
    var text = $input.val();
    $.post(
        '/amplio/reply/',
        {
            user_email: user_email,
            upon_feedback: feedback_id,
            upon_comment: -1,
            text: text
        },
        function (data) {
            if (data === 'OK') {
                location.reload(true);
            } else {
                console.log('OK was not returned');
            }
        }
    );
}

function removeImage() {
    $.post(
        '/amplio/remove-image/',
        {},
        function (data) {
            if (data === 'OK') {
                location.reload(true);
            } else {
                console.log('OK was not returned');
            }
        }
    )
}

function confirmDelete() {
    $('.ui.small.modal').modal('show');
}

function cancelDelete() {
    $('.ui.small.modal').modal('hide');
}