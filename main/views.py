from django.shortcuts import render

# Mock data for Rehubco Enterprise Operations OS

def dashboard(request):
    context = {
        'current_role': request.GET.get('role', 'executive'),
    }
    return render(request, 'main/dashboard.html', context)

def executive_dashboard(request):
    context = {
        'current_role': 'executive',
        'total_capacity': 45.8,
        'active_projects': 23,
        'regional_performance': [
            {'branch': 'Hargeisa', 'capacity_mw': 12.5, 'revenue': 850000, 'projects': 8, 'growth': 15},
            {'branch': 'Mogadishu', 'capacity_mw': 18.2, 'revenue': 1200000, 'projects': 10, 'growth': 22},
            {'branch': 'Ethiopia', 'capacity_mw': 10.1, 'revenue': 680000, 'projects': 4, 'growth': 18},
            {'branch': 'Djibouti', 'capacity_mw': 5.0, 'revenue': 420000, 'projects': 1, 'growth': 8},
        ],
        'revenue_vs_target': {
            'actual': 3150000,
            'target': 3500000,
            'percentage': 90
        },
        'inventory_warnings': [
            {'item': 'Solar Panels 450W', 'branch': 'Hargeisa', 'stock': 45, 'min': 100},
            {'item': 'Hybrid Inverter 10kW', 'branch': 'Mogadishu', 'stock': 8, 'min': 20},
            {'item': 'BESS Module 5kWh', 'branch': 'Ethiopia', 'stock': 12, 'min': 30},
        ],
        'workforce': {
            'total': 156,
            'field_technicians': 89,
            'engineers': 34,
            'sales': 18,
            'admin': 15
        }
    }
    return render(request, 'main/executive_dashboard.html', context)

def tendering_dashboard(request):
    context = {
        'current_role': 'tendering',
        'incoming_requests': [
            {'id': 'REQ-2026-089', 'client': 'City Hospital Complex', 'type': 'Hospital', 'capacity': '250kW', 'location': 'Mogadishu', 'status': 'New', 'date': '2026-10-18'},
            {'id': 'REQ-2026-088', 'client': 'Safari Hotel Group', 'type': 'Hotel', 'capacity': '180kW', 'location': 'Hargeisa', 'status': 'In Review', 'date': '2026-10-15'},
            {'id': 'REQ-2026-087', 'client': 'East Africa Bank HQ', 'type': 'Bank', 'capacity': '320kW', 'location': 'Djibouti', 'status': 'Proposal Sent', 'date': '2026-10-12'},
            {'id': 'REQ-2026-086', 'client': 'Supermarket Chain', 'type': 'Retail', 'capacity': '150kW', 'location': 'Addis Ababa', 'status': 'Negotiation', 'date': '2026-10-10'},
        ],
        'tender_tracking': [
            {'id': 'TEN-2026-045', 'title': 'UN Compound Solar Installation', 'client': 'UNDP', 'value': 450000, 'stage': 'Technical Evaluation', 'deadline': '2026-10-25'},
            {'id': 'TEN-2026-044', 'title': 'Port Authority Grid-Tie System', 'client': 'Djibouti Port', 'value': 890000, 'stage': 'Commercial Review', 'deadline': '2026-11-02'},
            {'id': 'TEN-2026-043', 'title': 'University Campus PV System', 'client': 'University of Hargeisa', 'value': 620000, 'stage': 'Awarded', 'deadline': '2026-10-20'},
        ],
        'historical_clients': [
            {'name': 'Golden Hotel', 'project': '150kW Hybrid System', 'value': 185000, 'completed': '2025-08', 'region': 'Hargeisa'},
            {'name': 'Safari Hospital', 'project': '200kW Grid-Tie System', 'value': 245000, 'completed': '2025-06', 'region': 'Mogadishu'},
            {'name': 'Dar Salaam Bank', 'project': '280kW Commercial PV', 'value': 340000, 'completed': '2025-04', 'region': 'Mogadishu'},
        ]
    }
    return render(request, 'main/tendering_dashboard.html', context)

def engineering_dashboard(request):
    context = {
        'current_role': 'engineering',
        'technical_blueprints': [
            {'id': 'BP-2026-034', 'project': 'City Hospital Complex', 'type': 'String Inverter Layout', 'status': 'In Progress', 'engineer': 'Ahmed Hassan', 'due': '2026-10-22'},
            {'id': 'BP-2026-033', 'project': 'Safari Hotel Group', 'type': 'PV Array Sizing', 'status': 'Completed', 'engineer': 'Fatima Omar', 'due': '2026-10-15'},
            {'id': 'BP-2026-032', 'project': 'East Africa Bank HQ', 'type': 'Single Line Diagram', 'status': 'Under Review', 'engineer': 'Mohamed Ali', 'due': '2026-10-18'},
        ],
        'site_surveys': [
            {'id': 'SS-2026-028', 'project': 'City Hospital Complex', 'location': 'Mogadishu', 'shading': 'Low', 'roof_area': '2500m²', 'ground_potential': 'High', 'surveyor': 'Yusuf Ibrahim', 'date': '2026-10-14'},
            {'id': 'SS-2026-027', 'project': 'Safari Hotel Group', 'location': 'Hargeisa', 'shading': 'Medium', 'roof_area': '1800m²', 'ground_potential': 'Medium', 'surveyor': 'Amina Mohamed', 'date': '2026-10-10'},
            {'id': 'SS-2026-026', 'project': 'East Africa Bank HQ', 'location': 'Djibouti', 'shading': 'None', 'roof_area': '3200m²', 'ground_potential': 'Low', 'surveyor': 'Hassan Warsame', 'date': '2026-10-08'},
        ],
        'commissioning_reports': [
            {'id': 'CR-2026-019', 'project': 'Golden Hotel Expansion', 'status': 'Passed', 'test_date': '2026-10-12', 'inspector': 'Technical Team A'},
            {'id': 'CR-2026-018', 'project': 'Safari Hospital Phase 2', 'status': 'Pending', 'test_date': '2026-10-18', 'inspector': 'Technical Team B'},
            {'id': 'CR-2026-017', 'project': 'Rural School Electrification', 'status': 'Failed', 'test_date': '2026-10-05', 'inspector': 'Technical Team A'},
        ]
    }
    return render(request, 'main/engineering_dashboard.html', context)

def procurement_dashboard(request):
    context = {
        'current_role': 'procurement',
        'inventory': [
            {'item': 'Solar Panel 450W Mono', 'part_no': 'PV-450M-XL', 'hargeisa': 250, 'mogadishu': 320, 'ethiopia': 180, 'djibouti': 95, 'total': 845, 'reorder': 500, 'status': 'OK'},
            {'item': 'Hybrid Inverter 10kW', 'part_no': 'INV-HYB-10K', 'hargeisa': 45, 'mogadishu': 38, 'ethiopia': 22, 'djibouti': 15, 'total': 120, 'reorder': 80, 'status': 'Warning'},
            {'item': 'BESS Module 5kWh', 'part_no': 'BESS-5K-LI', 'hargeisa': 60, 'mogadishu': 75, 'ethiopia': 35, 'djibouti': 20, 'total': 190, 'reorder': 150, 'status': 'Warning'},
            {'item': 'Mounting Structure Roof', 'part_no': 'MTN-ROOF-S', 'hargeisa': 180, 'mogadishu': 220, 'ethiopia': 140, 'djibouti': 80, 'total': 620, 'reorder': 400, 'status': 'OK'},
            {'item': 'Combiner Box 16-String', 'part_no': 'CBX-16S', 'hargeisa': 85, 'mogadishu': 95, 'ethiopia': 50, 'djibouti': 30, 'total': 260, 'reorder': 200, 'status': 'OK'},
            {'item': 'Cable 6mm² Solar', 'part_no': 'CBL-6MM-500', 'hargeisa': 5000, 'mogadishu': 6200, 'ethiopia': 3800, 'djibouti': 2500, 'total': 17500, 'reorder': 10000, 'status': 'OK'},
            {'item': 'MC4 Connector Set', 'part_no': 'MC4-SET', 'hargeisa': 3000, 'mogadishu': 3800, 'ethiopia': 2200, 'djibouti': 1500, 'total': 10500, 'reorder': 8000, 'status': 'Warning'},
        ],
        'incoming_shipments': [
            {'id': 'SHP-2026-034', 'supplier': 'Jinko Solar China', 'items': 'Solar Panels 450W x 500', 'eta': '2026-10-25', 'status': 'In Transit'},
            {'id': 'SHP-2026-033', 'supplier': 'Huawei Germany', 'items': 'Hybrid Inverters 10kW x 50', 'eta': '2026-10-28', 'status': 'Customs'},
            {'id': 'SHP-2026-032', 'supplier': 'Tesla Energy USA', 'items': 'BESS Modules 5kWh x 100', 'eta': '2026-11-02', 'status': 'Processing'},
        ]
    }
    return render(request, 'main/procurement_dashboard.html', context)

def finance_dashboard(request):
    context = {
        'current_role': 'finance',
        'milestone_billing': [
            {'project': 'City Hospital Complex', 'client': 'City Hospital', 'currency': 'USD', 'total': 450000, 'paid': 135000, 'pending': 315000, 'next_milestone': 'Installation 50%', 'due': '2026-10-30'},
            {'project': 'Safari Hotel Group', 'client': 'Safari Hotel', 'currency': 'USD', 'total': 280000, 'paid': 196000, 'pending': 84000, 'next_milestone': 'Final 10%', 'due': '2026-10-25'},
            {'project': 'East Africa Bank HQ', 'client': 'East Africa Bank', 'currency': 'USD', 'total': 520000, 'paid': 260000, 'pending': 260000, 'next_milestone': 'Commissioning 20%', 'due': '2026-11-05'},
        ],
        'project_costing': [
            {'project': 'City Hospital Complex', 'materials': 280000, 'labor': 85000, 'equipment': 45000, 'overhead': 40000, 'total': 450000, 'margin': 22},
            {'project': 'Safari Hotel Group', 'materials': 175000, 'labor': 52000, 'equipment': 28000, 'overhead': 25000, 'total': 280000, 'margin': 18},
        ],
        'supplier_invoices': [
            {'id': 'INV-2026-089', 'supplier': 'Jinko Solar China', 'amount': 125000, 'currency': 'USD', 'due': '2026-10-25', 'status': 'Pending'},
            {'id': 'INV-2026-088', 'supplier': 'Huawei Germany', 'amount': 89000, 'currency': 'EUR', 'due': '2026-10-22', 'status': 'Approved'},
            {'id': 'INV-2026-087', 'supplier': 'Local Steel Works', 'amount': 35000, 'currency': 'SOS', 'due': '2026-10-20', 'status': 'Paid'},
        ],
        'cash_flow': {
            'inflow': 892000,
            'outflow': 645000,
            'net': 247000,
            'forecast': 320000
        }
    }
    return render(request, 'main/finance_dashboard.html', context)

def hr_dashboard(request):
    context = {
        'current_role': 'hr',
        'employees': [
            {'id': 'EMP-001', 'name': 'Ahmed Hassan', 'role': 'Senior Engineer', 'department': 'Engineering', 'branch': 'Hargeisa', 'status': 'Active', 'certifications': 'PMP, PV Design Expert'},
            {'id': 'EMP-002', 'name': 'Fatima Omar', 'role': 'Field Technician Lead', 'department': 'Engineering', 'branch': 'Mogadishu', 'status': 'Active', 'certifications': 'Electrical Safety, PV Installation'},
            {'id': 'EMP-003', 'name': 'Mohamed Ali', 'role': 'Sales Manager', 'department': 'Tendering', 'branch': 'Hargeisa', 'status': 'Active', 'certifications': 'Business Development'},
            {'id': 'EMP-004', 'name': 'Amina Mohamed', 'role': 'Procurement Officer', 'department': 'Procurement', 'branch': 'Ethiopia', 'status': 'On Leave', 'certifications': 'Supply Chain Management'},
            {'id': 'EMP-005', 'name': 'Yusuf Ibrahim', 'role': 'Financial Analyst', 'department': 'Finance', 'branch': 'Mogadishu', 'status': 'Active', 'certifications': 'CPA, ACCA'},
            {'id': 'EMP-006', 'name': 'Hassan Warsame', 'role': 'HR Manager', 'department': 'HR', 'branch': 'Hargeisa', 'status': 'Active', 'certifications': 'HR Professional'},
        ],
        'attendance': [
            {'date': '2026-10-20', 'present': 142, 'absent': 8, 'late': 6, 'on_leave': 5},
            {'date': '2026-10-19', 'present': 145, 'absent': 5, 'late': 4, 'on_leave': 7},
            {'date': '2026-10-18', 'present': 148, 'absent': 3, 'late': 3, 'on_leave': 7},
        ],
        'field_schedule': [
            {'id': 'FS-2026-089', 'technician': 'Fatima Omar', 'project': 'City Hospital Complex', 'location': 'Mogadishu', 'date': '2026-10-21', 'task': 'Installation Phase 2'},
            {'id': 'FS-2026-088', 'technician': 'Ali Abdi', 'project': 'Safari Hotel Group', 'location': 'Hargeisa', 'date': '2026-10-22', 'task': 'Commissioning Test'},
            {'id': 'FS-2026-087', 'technician': 'Omar Hassan', 'project': 'East Africa Bank HQ', 'location': 'Djibouti', 'date': '2026-10-23', 'task': 'Site Survey'},
        ]
    }
    return render(request, 'main/hr_dashboard.html', context)

def project_pipeline(request):
    context = {
        'current_role': 'executive',
        'stages': {
            'Tender / Inquiry': [
                {'id': 'PRJ-2026-098', 'name': 'Ministry of Health HQ', 'client': 'Government', 'capacity': '350kW', 'location': 'Mogadishu', 'value': 420000, 'priority': 'High'},
                {'id': 'PRJ-2026-097', 'name': 'International School Campus', 'client': 'Education', 'capacity': '200kW', 'location': 'Hargeisa', 'value': 240000, 'priority': 'Medium'},
            ],
            'Site Survey': [
                {'id': 'PRJ-2026-096', 'name': 'City Hospital Complex', 'client': 'Healthcare', 'capacity': '250kW', 'location': 'Mogadishu', 'value': 300000, 'priority': 'High'},
                {'id': 'PRJ-2026-095', 'name': 'Safari Hotel Group', 'client': 'Hospitality', 'capacity': '180kW', 'location': 'Hargeisa', 'value': 215000, 'priority': 'Medium'},
            ],
            'Engineering Design': [
                {'id': 'PRJ-2026-094', 'name': 'East Africa Bank HQ', 'client': 'Banking', 'capacity': '320kW', 'location': 'Djibouti', 'value': 380000, 'priority': 'High'},
            ],
            'Procurement': [
                {'id': 'PRJ-2026-093', 'name': 'University Campus Phase 1', 'client': 'Education', 'capacity': '280kW', 'location': 'Addis Ababa', 'value': 335000, 'priority': 'Medium'},
            ],
            'Installation': [
                {'id': 'PRJ-2026-092', 'name': 'Supermarket Chain Branch 5', 'client': 'Retail', 'capacity': '150kW', 'location': 'Mogadishu', 'value': 180000, 'priority': 'High'},
                {'id': 'PRJ-2026-091', 'name': 'Industrial Factory Complex', 'client': 'Manufacturing', 'capacity': '450kW', 'location': 'Ethiopia', 'value': 540000, 'priority': 'High'},
            ],
            'Commissioning & Testing': [
                {'id': 'PRJ-2026-090', 'name': 'Golden Hotel Expansion', 'client': 'Hospitality', 'capacity': '100kW', 'location': 'Hargeisa', 'value': 120000, 'priority': 'Medium'},
            ],
        }
    }
    return render(request, 'main/project_pipeline.html', context)

def inventory_grid(request):
    context = {
        'current_role': 'procurement',
        'inventory': [
            {'item': 'Solar Panel 450W Mono', 'part_no': 'PV-450M-XL', 'hargeisa': 250, 'mogadishu': 320, 'ethiopia': 180, 'djibouti': 95, 'total': 845, 'reorder': 500, 'status': 'OK'},
            {'item': 'Hybrid Inverter 10kW', 'part_no': 'INV-HYB-10K', 'hargeisa': 45, 'mogadishu': 38, 'ethiopia': 22, 'djibouti': 15, 'total': 120, 'reorder': 80, 'status': 'Warning'},
            {'item': 'BESS Module 5kWh', 'part_no': 'BESS-5K-LI', 'hargeisa': 60, 'mogadishu': 75, 'ethiopia': 35, 'djibouti': 20, 'total': 190, 'reorder': 150, 'status': 'Warning'},
            {'item': 'Mounting Structure Roof', 'part_no': 'MTN-ROOF-S', 'hargeisa': 180, 'mogadishu': 220, 'ethiopia': 140, 'djibouti': 80, 'total': 620, 'reorder': 400, 'status': 'OK'},
            {'item': 'Combiner Box 16-String', 'part_no': 'CBX-16S', 'hargeisa': 85, 'mogadishu': 95, 'ethiopia': 50, 'djibouti': 30, 'total': 260, 'reorder': 200, 'status': 'OK'},
            {'item': 'Cable 6mm² Solar', 'part_no': 'CBL-6MM-500', 'hargeisa': 5000, 'mogadishu': 6200, 'ethiopia': 3800, 'djibouti': 2500, 'total': 17500, 'reorder': 10000, 'status': 'OK'},
            {'item': 'MC4 Connector Set', 'part_no': 'MC4-SET', 'hargeisa': 3000, 'mogadishu': 3800, 'ethiopia': 2200, 'djibouti': 1500, 'total': 10500, 'reorder': 8000, 'status': 'Warning'},
            {'item': 'DC Breaker 250A', 'part_no': 'BRK-DC-250', 'hargeisa': 120, 'mogadishu': 150, 'ethiopia': 85, 'djibouti': 45, 'total': 400, 'reorder': 300, 'status': 'OK'},
            {'item': 'AC Distribution Board', 'part_no': 'ADB-3P-63A', 'hargeisa': 65, 'mogadishu': 78, 'ethiopia': 42, 'djibouti': 28, 'total': 213, 'reorder': 150, 'status': 'OK'},
            {'item': 'Lightning Protection Kit', 'part_no': 'LP-PRO-KIT', 'hargeisa': 35, 'mogadishu': 42, 'ethiopia': 25, 'djibouti': 15, 'total': 117, 'reorder': 100, 'status': 'Warning'},
        ]
    }
    return render(request, 'main/inventory_grid.html', context)

def branch_selector(request):
    context = {
        'current_role': 'executive',
        'branches': [
            {'name': 'Hargeisa', 'country': 'Somaliland', 'coordinates': [9.56, 44.06], 'capacity_mw': 12.5, 'projects': 8, 'staff': 52, 'revenue': 850000, 'status': 'Active'},
            {'name': 'Mogadishu', 'country': 'Somalia', 'coordinates': [2.04, 45.32], 'capacity_mw': 18.2, 'projects': 10, 'staff': 68, 'revenue': 1200000, 'status': 'Active'},
            {'name': 'Addis Ababa', 'country': 'Ethiopia', 'coordinates': [9.02, 38.75], 'capacity_mw': 10.1, 'projects': 4, 'staff': 28, 'revenue': 680000, 'status': 'Active'},
            {'name': 'Djibouti City', 'country': 'Djibouti', 'coordinates': [11.83, 42.60], 'capacity_mw': 5.0, 'projects': 1, 'staff': 8, 'revenue': 420000, 'status': 'Active'},
        ]
    }
    return render(request, 'main/branch_selector.html', context)

