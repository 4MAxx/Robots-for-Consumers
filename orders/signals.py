from django.db.models.signals import post_save
from django.dispatch import receiver

from robots.models import Robot
from orders.services import send_email_to_customer, get_customer_email_and_pending_order_id, deactivate_pending_order


@receiver(post_save, sender=Robot)
def robot_for_pending_order_check(created, **kwargs):
    instance = kwargs['instance']
    robot_serial = instance.serial
    customer_email, pending_order_id = get_customer_email_and_pending_order_id(robot_serial)
    if created and customer_email:
        send_email_to_customer(customer_email, robot_serial)
        deactivate_pending_order(pending_order_id)