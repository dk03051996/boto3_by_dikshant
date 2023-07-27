    import boto3
    import datetime
    client = boto3.client('ec2',region_name='us-east-1')
    snapshots = client.describe_snapshots(OwnerIds=['405744707053'])
    for snapshot in snapshots['Snapshots']:
       a= snapshot['StartTime']
       b=a.date()
       c=datetime.datetime.now().date()
       d=c-b
       try:
        if d.days>30:
           id = snapshot['SnapshotId']
           client.delete_snapshot(SnapshotId=id)
       except Exception,e:
        if 'InvalidSnapshot.InUse' in e.message:
           print ("skipping this snapshot")
           continue


#I am testing this to delete snapshots that is not attached with any ami
