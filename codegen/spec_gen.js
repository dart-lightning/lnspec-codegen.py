function towire_onionmsg_path(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_point(value["node_id"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["enctlv"].length)]);

    _n += 1
    for (let v of value["enctlv"]) {
        buf = Buffer.concat([buf, towire_byte(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_onionmsg_path(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_blinded_path(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_point(value["blinding"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["path"].length)]);

    _n += 1
    for (let v of value["path"]) {
        buf = Buffer.concat([buf, towire_onionmsg_path(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_blinded_path(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_blinded_payinfo(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u32(value["fee_base_msat"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u32(value["fee_proportional_millionths"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["cltv_expiry_delta"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["features"].length)]);

    _n += 1
    for (let v of value["features"]) {
        buf = Buffer.concat([buf, towire_byte(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_blinded_payinfo(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_fallback_address(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_byte(value["version"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["address"].length)]);

    _n += 1
    for (let v of value["address"]) {
        buf = Buffer.concat([buf, towire_byte(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_fallback_address(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_invalid_realm(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    assert(value.length == _n);
    return buf;
}

function fromwire_invalid_realm(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_temporary_node_failure(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    assert(value.length == _n);
    return buf;
}

function fromwire_temporary_node_failure(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_permanent_node_failure(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    assert(value.length == _n);
    return buf;
}

function fromwire_permanent_node_failure(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_required_node_feature_missing(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    assert(value.length == _n);
    return buf;
}

function fromwire_required_node_feature_missing(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_invalid_onion_version(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_sha256(value["sha256_of_onion"])]);
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_invalid_onion_version(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_invalid_onion_hmac(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_sha256(value["sha256_of_onion"])]);
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_invalid_onion_hmac(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_invalid_onion_key(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_sha256(value["sha256_of_onion"])]);
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_invalid_onion_key(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_temporary_channel_failure(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u16(value["channel_update"].length)]);

    _n += 1
    for (let v of value["channel_update"]) {
        buf = Buffer.concat([buf, towire_byte(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_temporary_channel_failure(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_permanent_channel_failure(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    assert(value.length == _n);
    return buf;
}

function fromwire_permanent_channel_failure(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_required_channel_feature_missing(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    assert(value.length == _n);
    return buf;
}

function fromwire_required_channel_feature_missing(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_unknown_next_peer(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    assert(value.length == _n);
    return buf;
}

function fromwire_unknown_next_peer(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_amount_below_minimum(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u64(value["htlc_msat"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["channel_update"].length)]);

    _n += 1
    for (let v of value["channel_update"]) {
        buf = Buffer.concat([buf, towire_byte(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_amount_below_minimum(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_fee_insufficient(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u64(value["htlc_msat"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["channel_update"].length)]);

    _n += 1
    for (let v of value["channel_update"]) {
        buf = Buffer.concat([buf, towire_byte(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_fee_insufficient(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_incorrect_cltv_expiry(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u32(value["cltv_expiry"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["channel_update"].length)]);

    _n += 1
    for (let v of value["channel_update"]) {
        buf = Buffer.concat([buf, towire_byte(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_incorrect_cltv_expiry(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_expiry_too_soon(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u16(value["channel_update"].length)]);

    _n += 1
    for (let v of value["channel_update"]) {
        buf = Buffer.concat([buf, towire_byte(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_expiry_too_soon(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_incorrect_or_unknown_payment_details(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u64(value["htlc_msat"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u32(value["height"])]);
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_incorrect_or_unknown_payment_details(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_final_incorrect_cltv_expiry(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u32(value["cltv_expiry"])]);
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_final_incorrect_cltv_expiry(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_final_incorrect_htlc_amount(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u64(value["incoming_htlc_amt"])]);
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_final_incorrect_htlc_amount(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_channel_disabled(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_u16(value["flags"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["channel_update"].length)]);

    _n += 1
    for (let v of value["channel_update"]) {
        buf = Buffer.concat([buf, towire_byte(v)]);
    }
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_channel_disabled(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_expiry_too_far(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    assert(value.length == _n);
    return buf;
}

function fromwire_expiry_too_far(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_invalid_onion_payload(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    buf = Buffer.concat([buf, towire_bigsize(value["type"])]);
    _n += 1
    buf = Buffer.concat([buf, towire_u16(value["offset"])]);
    _n += 1
    assert(value.length == _n);
    return buf;
}

function fromwire_invalid_onion_payload(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

function towire_mpp_timeout(value)
{
    let _n = 0;
    let buf = Buffer.alloc(0);
    assert(value.length == _n);
    return buf;
}

function fromwire_mpp_timeout(buffer)
{
    let _n = 0;
    let retarr;
    value = {};

    return [value, buffer];
}

