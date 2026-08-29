// @odoo-module
import {PosOrder} from "@point_of_sale/app/models/pos_order";
import {patch} from "@web/core/utils/patch";

patch(PosOrder.prototype,{
    get loyaltyPoint(){
        console.log("This is data",this.priceIncl);
        return (this.priceIncl/10);
    },
});
