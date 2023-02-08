from django.core.mail import send_mail

from orders.models import PendingOrder


def create_pending_order(order_id, robot_serial):
    pending_order = PendingOrder(order_id=order_id, robot_serial=robot_serial)
    pending_order.save()


def get_customer_email_and_pending_order_id(robot_serial):
    pending_orders = PendingOrder.objects.filter(is_active=True, robot_serial=robot_serial)
    priority_pending_order = pending_orders.order_by('id').first()
    if priority_pending_order:
        customer_email = priority_pending_order.order.customer.email
        pending_order_id = priority_pending_order.id
        return customer_email, pending_order_id
    else:
        return (None, None)


def deactivate_pending_order(pending_order_id):
    PendingOrder.objects.filter(id=pending_order_id).update(is_active=False)


def send_email_to_customer(customer_email, robot_serial):
    model, version = robot_serial.split('-')
    subject = f'Уведомление о наличие робота серии {robot_serial}'
    message = f'Добрый день!\n' \
              f'Недавно вы интересовались нашим роботом модели {model}, версии {version}.\n' \
              f'Этот робот теперь в наличии. ' \
              f'Если вам подходит этот вариант - пожалуйста, свяжитесь с нами'
    send_mail(
        subject=subject,
        message=message,
        from_email='test@test.com',
        recipient_list=[customer_email],
    )