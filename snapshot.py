from genie.testbed import load
import getpass

def create_snapshot(device, feature, snapshot_name):
    device.connect(log_stdout=False)
    learned = device.learn(feature)
    learned.save(snapshot_name)
    print(f"✅ Snapshot saved: {snapshot_name}")

def main():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    testbed = load('testbed_files/gib.yaml')
    features = ['bgp', 'interface', 'routing']

    for device in testbed.devices.values():
        device.credentials['default']['username'] = username
        device.credentials['default']['password'] = password
        for feature in features:
            snapshot_name = f"{device.name}_{feature}_golden"
            create_snapshot(device, feature, snapshot_name)

if __name__ == "__main__":
    main()
