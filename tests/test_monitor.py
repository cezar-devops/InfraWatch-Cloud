ALERT_THRESHOLD = 80

def resource_alert(cpu, ram, disk):
    return any(
        value > ALERT_THRESHOLD
        for value in (cpu, ram, disk)
    )

def test_normal_usage():
    assert resource_alert(30, 50, 60) is False

def test_high_cpu():
    assert resource_alert(90, 50, 60) is True

def test_high_ram():
    assert resource_alert(30, 90, 60) is True

def test_high_disk():
    assert resource_alert(30, 50, 95) is True