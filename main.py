from functions.box_optimizer import box

strings = ['material_a.csv',
                'material_b.csv']

box_object = box(strings)
import pdb;pdb.set_trace()
box_object.optimize()

print(box_object.op_vals)
