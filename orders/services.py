from orders.models import PendingOrder


def create_pending_order(order_id):
    pending_order = PendingOrder(order_id=order_id)
    pending_order.save()