from django.shortcuts import render

# VRC - Vertical Redundancy Check (Even parity)
def vrc(data):
    ones = data.count('1')
    parity_bit = '0' if ones % 2 == 0 else '1'
    return data + parity_bit


# LRC - Longitudinal Redundancy Check
def lrc(data_list):
    if not data_list:
        return ""
    n = len(data_list[0])
    lrc_bits = ''
    for i in range(n):
        ones = sum(int(data[i]) for data in data_list)
        lrc_bits += '0' if ones % 2 == 0 else '1'
    return lrc_bits


# 2-D Parity
def two_d_parity(vrc_list):
    data_without_row_parity = [v[:-1] for v in vrc_list]
    col_parity = lrc(data_without_row_parity)
    last_col_parity = lrc([v[-1] for v in vrc_list])
    last_row = col_parity + last_col_parity
    return vrc_list + [last_row]


# Checksum with ADDITION STEPS
def checksum_verbose(data_list):
    bit_len = max(len(d) for d in data_list)

    steps = []
    total = 0

    # Step-by-step addition
    for d in data_list:
        steps.append(d.zfill(bit_len))
        total += int(d, 2)

    # Carry wrap-around
    while total >= 2 ** bit_len:
        carry = total >> bit_len
        total = (total & (2 ** bit_len - 1)) + carry

    final_sum = bin(total)[2:].zfill(bit_len)

    # 1's complement
    checksum = ''.join('1' if b == '0' else '0' for b in final_sum)

    return {
        "steps": steps,
        "final_sum": final_sum,
        "checksum": checksum
    }



# Django View
def error_detection(request):
    result = {}

    if request.method == "POST":
        dataset_input = request.POST.get('dataset', '').strip()

        if not dataset_input:
            result['error'] = "Please enter a dataset!"
        else:
            dataset = dataset_input.split()

            # Validate binary input
            for d in dataset:
                if not all(c in '01' for c in d):
                    result['error'] = f"Invalid binary number: {d}"
                    return render(request, 'main/error_detection.html', {'result': result})

            # VRC
            vrc_list = [vrc(d) for d in dataset]

            # LRC
            lrc_row = lrc(dataset)
            lrc_full = dataset + [lrc_row]

            # 2-D Parity
            two_d = two_d_parity(vrc_list)

            # Checksum with steps
            cs_data = checksum_verbose(dataset)

            result['VRC'] = vrc_list
            result['LRC'] = lrc_full
            result['TwoD'] = two_d
            result['ChecksumSteps'] = cs_data['steps']
            result['ChecksumSum'] = cs_data['final_sum']
            result['Checksum'] = cs_data['checksum']

    return render(request, 'main/error_detection.html', {'result': result})
