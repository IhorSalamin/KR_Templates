from app.db import Database

class MessageInstance:
    def __init__(self, MessageID, MessageTime, MessageSenderRef, MessageRecipientRef, MessagePriority, MessageContext, MessageAttachments, MessageBookingRef):
        self.message_id = MessageID
        self.message_time = MessageTime
        self.message_sender_ref = MessageSenderRef
        self.message_recipient_ref = MessageRecipientRef
        self.message_priority = MessagePriority
        self.message_context = MessageContext
        self.message_attachments = MessageAttachments
        self.message_booking_ref = MessageBookingRef

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
    def add_message(MessageTime, MessageSenderRef, MessageRecipientRef, MessagePriority, MessageContext, MessageAttachments, MessageBookingRef):
        db = Database()
        query = """
        INSERT INTO Messages (MessageTime, MessageSenderRef, MessageRecipientRef, MessagePriority, MessageContext, MessageAttachments, MessageBookingRef)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        db.execute_query(query, (MessageTime, MessageSenderRef, MessageRecipientRef, MessagePriority, MessageContext, MessageAttachments, MessageBookingRef))
