from circularis.base.communication import SBJ_REQUEST, MSG_REQUEST, SBJ_REJECT, MSG_REJECT, SBJ_ACCEPT, MSG_ACCEPT
from circularis.messaging.models import MessageOneOne, MessageType


def send_book_message(sender, receiver, book, subject, message, msg_type):
    msg = MessageOneOne()
    msg.sender = sender
    msg.msg_type = msg_type
    msg.receiver = receiver
    msg.book = book
    msg.subject = subject
    msg.content = message % (book.title, msg.sender)
    msg.save()


def process_book_request(request, book):
    book.put_in_hold()
    msg_type = MessageType.objects.get(code=MessageType.MessageTypeOptions.RQ)
    send_book_message(request.user, book.user, book, SBJ_REQUEST, MSG_REQUEST, msg_type)
    book.save()
    return True


def process_book_reject_request(request, message):
    book = message.book
    book.remove_hold()
    msg_type = MessageType.objects.get(code=MessageType.MessageTypeOptions.RJ)
    send_book_message(request.user, message.sender, book, SBJ_REJECT, MSG_REJECT, msg_type)
    book.save()
    process_delete_message(request, message)
    return True


def process_delete_message(request, msg):
    msg.delete()
    return True


def process_accept_request(request, message):
    book = message.book
    book.remove_hold()  # !!!
    book.user = message.sender
    msg_type = MessageType.objects.get(code=MessageType.MessageTypeOptions.AC)
    send_book_message(request.user, message.sender, book, SBJ_ACCEPT, MSG_ACCEPT, msg_type)
    book.save()
    process_delete_message(request, message)
    return True
