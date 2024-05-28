from db import Database

class MessageInstance:
    def __init__(self, message_id, message_time, message_sender_ref, message_recipient_ref, message_priority, message_context, message_attachments, message_booking_ref):
        self.message_id = message_id
        self.message_time = message_time
        self.message_sender_ref = message_sender_ref
        self.message_recipient_ref = message_recipient_ref
        self.message_priority = message_priority
        self.message_context = message_context
        self.message_attachments = message_attachments
        self.message_booking_ref = message_booking_ref

class Message:
    @staticmethod
    def get_all_messages():
        db = Database()
        query = "SELECT * FROM Messages"
        results = db.execute_query(query)
        messages = []
        for row in results:
            messages.append(MessageInstance(**row))
        return messages

    @staticmethod
    def add_message(message_time, message_sender_ref, message_recipient_ref, message_priority, message_context, message_attachments, message_booking_ref):
        db = Database()
        query = """
        INSERT INTO Messages (MessageTime, MessageSenderRef, MessageRecipientRef, MessagePriority, MessageContext, MessageAttachments, MessageBookingRef)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        db.execute_query(query, (message_time, message_sender_ref, message_recipient_ref, message_priority, message_context, message_attachments, message_booking_ref))
