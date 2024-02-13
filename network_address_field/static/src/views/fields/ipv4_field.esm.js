/** @odoo-module **/
import {Component, useRef} from "@odoo/owl";
import {_t} from "@web/core/l10n/translation";
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
    static template = "network_address_field.IPv4Field";
    static props = {
        ...standardFieldProps,
        placeholder: {type: String, optional: true},
        maxLength: {type: Number, optional: true},
        regex: {type: Object, optional: true},
        formatter: {type: Function, optional: true},
    };
    static defaultProps = {
        shouldTrim: true,
    };

    setup() {
        this.input = useRef("input");
        useInputField({
            getValue: () => this.formattedValue,
            parse: (v) => this.parse(v),
        });
    }

    get value() {
      return this.props.record.data[this.props.name];
    }

    get formattedValue() {
        return this.props.formatter(this.value);
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

export const ipv4Field = {
    component: IPv4Field,
    supportedTypes: ["ipv4_host", "ipv4_network"],
    displayName: _t("IPv4Field"),
    extractProps: ({attrs}) => {
        const maxLength = 15 + 3;
        const regex = /^.+$/;
        const formatter = formatIPv4;

        return {
            placeholder: attrs.placeholder,
            maxLength,
            regex,
            formatter,
        };
    },
};

registry.category("fields").add("ipv4_host", ipv4Field);
registry.category("fields").add("ipv4_network", ipv4Field);
formatters.add("ipv4_host", formatIPv4);
formatters.add("ipv4_network", formatIPv4);
