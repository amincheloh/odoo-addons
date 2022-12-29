/** @odoo-module **/
import {Component, useRef} from "@odoo/owl";
import {registry} from "@web/core/registry";
import {standardFieldProps} from "@web/views/fields/standard_field_props";
import {useInputField} from "@web/views/fields/input_field_hook";

const formatters = registry.category("formatters");

export function formatIPv4(value) {
    if (!value) {
        return "";
    }

    return value;
}

export class IPv4Field extends Component {
    setup() {
        this.input = useRef("input");
        useInputField({
            getValue: () => this.formattedValue,
            parse: (v) => this.parse(v),
        });
    }

    get formattedValue() {
        return this.props.formatter(this.props.value);
    }

    parse(value) {
        let v = value;
        if (this.props.shouldTrim) {
            v = v.trim();
        }

        const regex = this.props.regex;
        if (regex.exec(v) === null) {
            throw new Error("Pattern mismatched");
        }

        return v;
    }
}

IPv4Field.template = "network_address_field.IPv4Field";
IPv4Field.defaultProps = {
    shouldTrim: true,
};
IPv4Field.props = {
    ...standardFieldProps,
    placeholder: {type: String, optional: true},
    maxLength: {type: Number, optional: true},
    regex: {type: Object, optional: true},
    formatter: {type: Function, optional: true},
};
IPv4Field.extractProps = ({attrs, field}) => {
    let maxLength = 15;
    const regex = /^.+$/;
    const formatter = formatIPv4;
    if (field.type === "ipv4_network") {
        maxLength = 15 + 3;
    }

    return {
        placeholder: attrs.placeholder,
        maxLength,
        regex,
        formatter,
    };
};
IPv4Field.supportedTypes = ["ipv4_host", "ipv4_network"];
registry.category("fields").add("ipv4_host", IPv4Field);
registry.category("fields").add("ipv4_network", IPv4Field);
formatters.add("ipv4_host", formatIPv4);
formatters.add("ipv4_network", formatIPv4);
