from genie.testbed import load
import getpass
from unittest import enterModuleContext

def create_snapshot(device, feature, snapshot_name):
    device.connect(log_stdout=False, debug=True)
    learned = device.learn(feature)
    learned.save(snapshot_name)
    print(f"✅ Snapshot saved: {snapshot_name}")

def main():
    enter_password = input("Do you want to enter password? (y/n): ").lower()
    use_password = enter_password == 'y'
    
    if use_password:
        username = input("Username: ")
        password = getpass.getpass("Password: ")
    testbed = load('./testbed_files/gib.yaml')
    features = ['bgp', 'interface', 'routing']

    for device in testbed.devices.values():
        if enter_password == 'y'.lower():
            device.credentials['default']['username'] = username
            device.credentials['default']['password'] = password
        for feature in features:
            snapshot_name = f"{device.name}_{feature}_golden"
            create_snapshot(device, feature, snapshot_name)

if __name__ == "__main__":
    main()
