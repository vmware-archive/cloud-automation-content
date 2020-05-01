### Author(s)
  - James Wirth

### Summary
This blueprint deploys a vSphere Event Broker Appliance (VEBA) from an .ova that is available via http. In this case it's hosted on an Minio based object server. As part of the deployment the VEBA is connected to an existing vCenter.

### Usage:
This Blueprint can be launched manually but it's often preferrable to launch via Code Stream such that the inputs can be added in the COde Stream pipeline rather than having to type them in each time.