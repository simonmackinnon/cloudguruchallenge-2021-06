from aws_cdk.aws_ec2 import RouterType, CfnSecurityGroup

# basic VPC configs
VPC = 'custom-vpc'

INTERNET_GATEWAY = 'internet-gateway'

REGION = 'ap-southeast-2'

# route tables
PUBLIC_ROUTE_TABLE = 'public-route-table'

ROUTE_TABLES_ID_TO_ROUTES_MAP = {
    PUBLIC_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'gateway_id': INTERNET_GATEWAY,
            'router_type': RouterType.GATEWAY
        }
    ],
}

# security groups
SECURITY_GROUP = 'python_web_app_sg'

SECURITY_GROUP_ID_TO_CONFIG = {
    SECURITY_GROUP: {
        'group_description': 'SG of the Python Test Web App servers',
        'group_name': SECURITY_GROUP,
        'security_group_ingress': [
            CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ip='0.0.0.0/0', from_port=80, to_port=80
            ),
            CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ipv6='::/0', from_port=80, to_port=80
            ),
            CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ip='0.0.0.0/0', from_port=443, to_port=443
            ),
            CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ipv6='::/0', from_port=443, to_port=443
            ),
            CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ip='0.0.0.0/0', from_port=22, to_port=22
            ),
            CfnSecurityGroup.IngressProperty(
                ip_protocol='TCP', cidr_ipv6='::/0', from_port=22, to_port=22
            ),
        ],
        'tags': [{'key': 'Name', 'value': SECURITY_GROUP}]
    },
}

# subnets and instances
PUBLIC_SUBNET_1 = 'public-subnet-1'
PUBLIC_SUBNET_2 = 'public-subnet-2'
PRIVATE_SUBNET_1 = 'private-subnet-1'
PRIVATE_SUBNET_2 = 'private-subnet-2'


SUBNET_CONFIGURATION = {
    PUBLIC_SUBNET_1: {
        'availability_zone': 'ap-southeast-2a', 'cidr_block': '10.0.1.0/24', 'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE,
    },
    PUBLIC_SUBNET_2: {
        'availability_zone': 'ap-southeast-2b', 'cidr_block': '10.0.2.0/24', 'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE,
    },
    PRIVATE_SUBNET_1: {
        'availability_zone': 'ap-southeast-2a', 'cidr_block': '10.0.3.0/24', 'map_public_ip_on_launch': False,
        'route_table_id': PUBLIC_ROUTE_TABLE,
    },
    PRIVATE_SUBNET_2: {
        'availability_zone': 'ap-southeast-2b', 'cidr_block': '10.0.4.0/24', 'map_public_ip_on_launch': False,
        'route_table_id': PUBLIC_ROUTE_TABLE,
    }
}
