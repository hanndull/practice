def chop_sms(sms, max_len):
    # slice into the sms message in chunks by len of max_len, 
    #   essentially need to paginate thru

    total = len(sms)
    rounds = total//max_len
    extra_slice = total % max_len

    sms_fragments = []
    pg_count = 1
    char_count = 0

    while pg_count < rounds + 1:
        fragment = sms[char_count:pg_count*max_len]
        sms_fragments.append((fragment, f"({pg_count}/{rounds +1})"))

        pg_count += 1
        char_count += max_len

    sms_fragments.append((sms[-extra_slice:], f"({pg_count}/{rounds +1})"))

    return sms_fragments

